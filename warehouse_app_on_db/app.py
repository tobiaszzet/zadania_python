from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask.views import MethodView
from sqlalchemy import text

with open('secret_key.txt', 'r') as file:
    password = file.read()

app = Flask(__name__, static_url_path='/static/css/')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///magazyn_db.db'
app.secret_key = 'password'
db = SQLAlchemy(app)


class Balance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Integer, nullable=False)
    commission = db.Column(db.Integer, nullable=False)


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    script = db.Column(db.String, nullable=False)
    script_date = db.Column(db.TEXT, nullable=False)


with app.app_context():
    db.create_all()
    try:
        balance_db = db.session.query(Balance).first()
        balance_var = balance_db.balance
        commission_var = balance_db.commission
    except AttributeError:
        balance = Balance(balance=0, commission=0)
        db.session.add(balance)
        db.session.commit()
        balance_db = db.session.query(Balance).first()
        balance_var = balance_db.balance
        commission_var = balance_db.commission

    products_list = db.session.query(Products).all()
    history_list = db.session.query(History).all()


class MainView(MethodView):
    @app.route("/", methods=["GET", "POST"])
    def main_view():
        global balance_var, products_list, history_list, commission_var

        if request.method == "GET":
            return render_template("home_page.html", **{
                        "products": products_list,
                        "commission": commission_var,
                        "balance": balance_var
            })
        else:
            try:
                request_type = request.form.get("request_type")
                if request_type == "sales_form":
                    handle_sales_form(request.form)
                    return render_template("home_page.html", **{
                        "products": products_list,
                        "commission": commission_var,
                        "balance": balance_var
                    })
                elif request_type == "balance_form":
                    input_balance = int(request.form.get("InputBalance"))
                    with app.app_context():
                        balance_in_db = db.session.query(Balance).first()
                        balance_in_db.balance = input_balance
                        balance_var = balance_in_db.balance
                        db.session.add(balance_in_db)
                        db.session.commit()

                    db_history_update(f"Zmieniono saldo na {input_balance} zł")

                    return render_template("home_page.html", **{
                        "products": products_list,
                        "commission": commission_var,
                        "balance": balance_var
                    })
                elif request_type == "commission_form":
                    input_commission = float(request.form.get("InputCommission"))
                    with app.app_context():
                        commission_in_db = db.session.query(Balance).first()
                        commission_in_db.commission = input_commission
                        commission_var = commission_in_db.commission
                        db.session.add(commission_in_db)
                        db.session.commit()

                    return render_template("home_page.html", **{
                        "products": products_list,
                        "commission": commission_var,
                        "balance": balance_var
                    })

                else:
                    input_product = request.form.get("produkt")
                    input_amount = int(request.form.get("sztuk"))
                    input_price = float(request.form.get("cena"))
                    product_in_warehouse = False

                    for item in products_list:
                        if item.product == input_product and (input_price * input_amount) <= balance_var:
                            product_in_warehouse = True
                            item.amount = item.amount + input_amount
                            item.price = input_price
                            balance_var = balance_var - (input_price * input_amount)
                            db_update(item, balance_var)
                            db_history_update(f"Kupiono {input_amount} szt. produktu {input_product} za {input_price} zł")
                        else:
                            continue

                    if not product_in_warehouse and input_price * input_amount <= balance_var:
                        product = Products(product=input_product, amount=input_amount, price=input_price)
                        balance_var = balance_var - (float(request.form.get("cena")) * int(request.form.get("sztuk")))
                        db_new_product(product, balance_var)
                        products_list = db.session.query(Products).all()
                        db_history_update(f"Kupiono {input_amount} szt. produktu {input_product} za {input_price} zł")

                    elif (not product_in_warehouse) and (input_price * input_amount) > balance_var:
                        flash("Nie masz wystarczających środków na koncie")
                return render_template("home_page.html", **{
                    "products": products_list,
                    "commission": commission_var,
                    "balance": balance_var
                })

            except ValueError:
                flash("coś nie pykło")
                return render_template("home_page.html", **{
                    "products": products_list,
                    "commission": commission_var,
                    "balance": balance_var
                })

    @app.route("/history/", methods=["GET", "POST"])
    def history():
        if request.method == "GET":
            return render_template("history.html", **{
                "history": history_list,
                "balance": balance_var,
                "commission": commission_var
                })
        else:
            try:
                index_length = len(history_list)
                input_from = int(request.form.get("od")) - 1
                input_to = int(request.form.get("do"))
                if input_from < 0 or input_to > index_length:
                    flash("Wprowadziłeś zakres spoza listy.")
                    return render_template("history.html", **{
                        "history": history_list,
                        "balance": balance_var,
                        "commission": commission_var
                    })

                else:
                    przeglad_part = history_list[input_from:input_to]
                    return render_template("history.html", **{
                        "history": przeglad_part,
                        "balance": balance_var,
                        "commission": commission_var
                    })

            except ValueError:
                flash("Nie wprowadzono danych. Zostanie wyświetlona cała lista")
                return render_template("history.html", **{
                    "history": history_list,
                    "balance": balance_var,
                    "commission": commission_var
                })

    @app.route("/ascending_price/", methods=["GET", "POST"])
    def ascending_price():
        asc_users_query = text("SELECT * FROM products ORDER BY price ASC;")
        sorted_products_asc = db.session.execute(asc_users_query)
        return render_template("home_page.html", **{
            "products": sorted_products_asc,
            "balance": balance_var,
            "commission": commission_var
        })

    @app.route("/descending_price/", methods=["GET", "POST"])
    def descending_price():
        desc_users_query = text("SELECT * FROM products ORDER BY price DESC;")
        sorted_products_desc = db.session.execute(desc_users_query)
        return render_template("home_page.html", **{
            "products": sorted_products_desc,
            "balance": balance_var,
            "commission": commission_var
        })

    @app.route("/ascending_amount/", methods=["GET", "POST"])
    def ascending_amount():
        asc_users_query = text("SELECT * FROM products ORDER BY amount ASC;")
        sorted_products_asc = db.session.execute(asc_users_query)
        return render_template("home_page.html", **{
            "products": sorted_products_asc,
            "balance": balance_var,
            "commission": commission_var
        })

    @app.route("/descending_amount/", methods=["GET", "POST"])
    def descending_amount():
        desc_users_query = text("SELECT * FROM products ORDER BY amount DESC;")
        sorted_products_desc = db.session.execute(desc_users_query)
        return render_template("home_page.html", **{
            "products": sorted_products_desc,
            "balance": balance_var,
            "commission": commission_var
        })


def handle_sales_form(form):
    global balance_var, products_list, commission_var
    input_product = request.form.get("produkt")
    input_amount = int(request.form.get("sztuk"))

    product_sold = False
    not_enough = False
    for item in products_list:
        if item.product == input_product:
            if item.amount - input_amount >= 0:
                item.amount = item.amount - input_amount
                price_gross = item.price + (item.price * commission_var / 100)
                balance_var += input_amount * price_gross
                db_update(item, balance_var)
                db_history_update(f"Sprzedano {input_amount} szt. produktu {input_product} za {price_gross} zł")
                product_sold = True

            elif (item.amount - input_amount) <= 0:
                not_enough = True
                flash("Niestety nie mamy tylu sztuk")
                break
        else:
            continue
    if not product_sold and not not_enough:
        flash("Nie mamy takiego produktu")


def db_new_product(product, balance_func):
    with app.app_context():
        balance_in_db = db.session.query(Balance).first()
        balance_in_db.balance = balance_func

        db.session.add(product, balance_in_db)
        db.session.commit()


def db_update(product_func, balance_func):
    with app.app_context():
        balance_in_db = db.session.query(Balance).first()
        balance_in_db.balance = balance_func

        product_in_db = db.session.query(Products).filter(Products.product == product_func.product).first()
        product_in_db.amount = product_func.amount
        product_in_db.price = product_func.price

        db.session.add(product_in_db, balance_in_db)
        db.session.commit()


def db_history_update(history_script):
    global history_list
    current_datetime = datetime.now()
    script_func = History(
        script=history_script,
        script_date=current_datetime.strftime('%Y-%m-%d %H:%M')
    )
    with app.app_context():
        db.session.add(script_func)
        db.session.commit()
        history_list = db.session.query(History).all()


if __name__ == "__main__":
    app.run(debug=True)
