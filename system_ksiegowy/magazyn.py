print("Witaj w sklepie Z MOTYKĄ NA ZIEMIĘ. Co chcesz zrobić?")
print("dostępne komendy:\n- saldo\n- sprzedaż\n- zakup\n- konto\n- lista\n- magazyn\n- przegląd\n- koniec")

from file_handler import FileHandler
instancja_file_handlera = FileHandler(file_with_balance_path= "saldo_konta.txt",
                                      file_with_warehouse_path= "stan_magazynu.json",
                                      file_with_history_path= "historia.txt")

saldo =  float(instancja_file_handlera.odczyt_danych_z_file_with_balance())
stan_magazynu = instancja_file_handlera.odczyt_danych_z_file_with_warehouse()

przeglad = instancja_file_handlera.odczyt_danych_file_with_history_path()
koniec = False

while not koniec:
    komenda = input("Wprowadź odpowiednią komendę: ")

    if komenda == "koniec":
        koniec = True
        print("zakończono program")
        instancja_file_handlera.zapis_do_plikow_balance_warehouse(budzet=str(saldo), stan_magazynu= stan_magazynu)
        instancja_file_handlera.zapis_historii(historia=przeglad)

    elif komenda == "saldo":
        wplata = float(input("Podaj kwotę, którą chcesz dodać lub wyciągnąć z konta: "))
        saldo += wplata
        przeglad.append(f"Do konta dodano {wplata} zl")

    elif komenda == "sprzedaż":
        sprzedawany_produkt = input("Jaki produkt chcesz sprzedać?: ")
        cena_sprzedawanego_prod = float(input("Podaj cenę produktu: "))
        sprzedanych_sztuk = int(input("Podaj liczbę sztuk: "))
        produkt_sprzedany = False
        for prod in stan_magazynu:
            if prod.get("nazwa_produktu") == sprzedawany_produkt:
                if (prod.get("sztuk") - sprzedanych_sztuk) >= 0:
                    prod["sztuk"] = prod["sztuk"] - sprzedanych_sztuk
                    saldo += sprzedanych_sztuk * cena_sprzedawanego_prod
                    przeglad.append(f"Sprzedano {sprzedanych_sztuk} sztuk produktu {sprzedawany_produkt} za {cena_sprzedawanego_prod} zl")
                    produkt_sprzedany = True
                elif (prod.get("sztuk") - sprzedanych_sztuk) <= 0:
                    print(f"Niestety nie mamy tylu sztuk w magazynie. Liczba dostępnych sztuk: {prod["sztuk"]}")
            else:
                continue
        if produkt_sprzedany == False:
            print("Nie mamy takiego produktu")

    elif komenda == "zakup":
        kupowany_produkt = input("Podaj nazwę produktu: ")
        cena_kupowanego_prod = float(input("Podaj cenę produktu: "))
        sztuk_kupowanego_prod = int(input("Podaj liczbę sztuk: "))
        produkt_w_magazynie = False
        for produkt in stan_magazynu:
            if produkt.get("nazwa_produktu") == kupowany_produkt and cena_kupowanego_prod * sztuk_kupowanego_prod <= saldo:
                produkt_w_magazynie = True
                produkt["sztuk"] = produkt["sztuk"] + sztuk_kupowanego_prod
                saldo = saldo - (cena_kupowanego_prod * sztuk_kupowanego_prod)
                przeglad.append(f"Kupiono {sztuk_kupowanego_prod} sztuk produktu {kupowany_produkt} za {cena_kupowanego_prod} zl")
                break
            else:
                continue
        if not produkt_w_magazynie and cena_kupowanego_prod * sztuk_kupowanego_prod <= saldo:
            stan_magazynu.append({
                "nazwa_produktu" : kupowany_produkt,
                "cena" : cena_kupowanego_prod,
                "sztuk" : sztuk_kupowanego_prod
            })
            przeglad.append(f"Kupiono {sztuk_kupowanego_prod} sztuk produktu {kupowany_produkt} za {cena_kupowanego_prod} zl")
            saldo = saldo - (cena_kupowanego_prod * sztuk_kupowanego_prod)
        elif (cena_kupowanego_prod * sztuk_kupowanego_prod) > saldo:
            print("Nie masz wystarczających środków na koncie na taki zakup.")
        else:
            continue


    elif komenda == "konto":
        print(f"Stan sklepowego konta wynosi: {saldo}")

    elif komenda == "lista":
        for produkt  in stan_magazynu:
            print(f"Oto aktualny stan magazynu \n{produkt}")

    elif komenda == "magazyn":
        produkt = input("Podaj nazwę produktu dla którego chcesz wyświetlić informacje: ")
        produkt_index = 0
        for prod in stan_magazynu:
            if prod.get("nazwa_produktu") == produkt:
                print(stan_magazynu[produkt_index])
                break
            else:
                produkt_index += 1
                continue

    elif komenda == "przegląd":
        od = (input("Podaj zakres. Od którego indeksu chcesz wyświetlić przegląd?: "))
        do = (input("Do którego?: "))
        indexy = len(przeglad)
        if od == "" or do == "":
            print(przeglad)
        elif (int(od) > indexy or  int(od) < 0) or int(do) > indexy:
            print(f"Wprowadziłeś zakres spoza listy. Liczba zapisanych akcji wynosi {indexy}")
        else:
            print(przeglad[int(od):int(do)])

    print("dostępne komendy:\n - saldo\n- sprzedaż\n- zakup\n- konto\n- lista\n- magazyn\n- przegląd\n- koniec")
