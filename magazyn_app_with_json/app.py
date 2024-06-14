from flask import Flask
from flask.views import MethodView
from flask import render_template, request
from file_handler import FileHandler

app = Flask(__name__, static_url_path='/static')

instancja_file_handlera = FileHandler(file_with_balance_path= "saldo_konta.txt",
                                      file_with_warehouse_path= "stan_magazynu.json",
                                      file_with_history_path= "historia.txt")

saldo =  float(instancja_file_handlera.odczyt_danych_z_file_with_balance())
stan_magazynu = instancja_file_handlera.odczyt_danych_z_file_with_warehouse()
przeglad = instancja_file_handlera.odczyt_danych_file_with_history_path()


class MainView(MethodView):
    @app.route("/", methods=["GET", "POST"])
    def main_view():
        global saldo, stan_magazynu
        if request.method == "GET":
            return render_template("home_page.html", **{
                "products": stan_magazynu,
                "balance": saldo
            })
        else:
            try:
                request_type = request.form.get("request_type")
                if request_type == "sales_form":
                    handle_sales_form(request.form)
                    return render_template("home_page.html", **{
                        "products": stan_magazynu,
                        "balance": saldo
                    })
                else:
                    input_product = request.form.get("produkt")
                    input_amount = int(request.form.get("sztuk"))
                    input_price = float(request.form.get("cena"))
                    product_in_warehouse = False
                    for product in stan_magazynu:
                        if product.get("nazwa_produktu") == input_product and input_price * input_amount <= saldo:
                            product_in_warehouse = True
                            product['sztuk'] = product["sztuk"] + input_amount
                            product["cena"] = input_price
                            saldo = saldo - (input_price * input_amount)
                            przeglad.append(
                                f"Kupiono {input_amount} sztuk produktu {input_product} za {input_price} zł"
                            )

                            break
                        else:
                            continue
                    if not product_in_warehouse and input_price * input_amount <= saldo:
                        stan_magazynu.append({
                            "nazwa_produktu": input_product,
                            "cena": input_price,
                            "sztuk": input_amount
                        })
                        saldo = saldo - (float(request.form.get("cena")) * float(request.form.get("sztuk")))
                        przeglad.append(
                            f"Kupiono {input_amount} sztuk produktu {input_product} za {input_price} zl"
                        )
                    elif (input_price * input_amount) > saldo:
                        print("Nie masz wystarczających środków na koncie")

                instancja_file_handlera.zapis_do_plikow_balance_warehouse(str(saldo), stan_magazynu)
                instancja_file_handlera.zapis_historii(przeglad)
                return render_template("home_page.html", **{
                    "products": stan_magazynu,
                    "balance": saldo
                })
            except ValueError:
                print("coś się popsuło")

    def handle_sales_form(form):
        global saldo, stan_magazynu
        produkt_sprzedany = False
        input_product = request.form.get("produkt")
        input_amount = int(request.form.get("sztuk"))
        input_price = float(request.form.get("cena"))

        for product in stan_magazynu:
            if product.get("nazwa_produktu") == input_product:
                if int(product.get("sztuk")) - input_amount >= 0:
                    product["sztuk"] = int(product["sztuk"]) - input_amount
                    saldo += input_amount * input_price
                    instancja_file_handlera.zapis_do_plikow_balance_warehouse(str(saldo), stan_magazynu)
                    przeglad.append(
                        f"Sprzedano {input_amount} sztuk produktu {input_product} za {input_price} zł")
                    produkt_sprzedany = True
                    instancja_file_handlera.zapis_historii(przeglad)
                elif (int(product.get("sztuk")) - input_amount) <= 0:
                    print("Niestety nie mamy tylu sztuk")
            else:
                continue
        if produkt_sprzedany == False:
            print("Nie mamy takiego produktu")

    @app.route("/history/", methods=["GET", "POST"])
    def history():
        przeglad_with_id = []
        counter = 0
        for post in przeglad:
            counter += 1
            post_with_counter = f"{counter}. {post}"
            przeglad_with_id.append(post_with_counter)

        if request.method == "GET":
            return render_template("history.html", history=przeglad_with_id)
        else:
            try:
                index_length = len(przeglad)
                input_from = int(request.form.get("od")) - 1
                input_to = int(request.form.get("do"))
                if input_from < 0 or input_to > index_length:
                    return render_template("history.html", history=przeglad_with_id)
                elif (input_from > index_length or input_from < 0) or input_to > index_length:
                    print("Wprowadziłeś zakres spoza listy.")
                else:
                    przeglad_part = przeglad_with_id[input_from:input_to]
                    return render_template("history.html", history=przeglad_part)

            except ValueError:
                print("Nie wprowadzono danych, zostanie wyświetlona cała lista")
                return render_template("history.html", history=przeglad_with_id)


if __name__ == "__main__":
    app.run(debug=True)
