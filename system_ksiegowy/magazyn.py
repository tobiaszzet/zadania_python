from manager import manager

print("Witaj w sklepie Z MOTYKĄ NA ZIEMIĘ. Co chcesz zrobić?")


@manager.assign("saldo")
def saldo(manager):
    wplata = float(input("Podaj kwotę, którą chcesz dodać lub wyciągnąć z konta: "))
    manager.saldo += wplata
    manager.przeglad.append(f"Do konta dodano {wplata} zl")


@manager.assign("sprzedaz")
def sprzedaz(manager):
    sprzedawany_produkt = input("Jaki produkt chcesz sprzedać?: ")
    cena_sprzedawanego_prod = float(input("Podaj cenę produktu: "))
    sprzedanych_sztuk = int(input("Podaj liczbę sztuk: "))
    produkt_sprzedany = False
    for prod in manager.stan_magazynu:
        if prod.get("nazwa_produktu") == sprzedawany_produkt:
            if (prod.get("sztuk") - sprzedanych_sztuk) >= 0:
                prod["sztuk"] = prod["sztuk"] - sprzedanych_sztuk
                manager.saldo += sprzedanych_sztuk * cena_sprzedawanego_prod
                manager.przeglad.append(
                    f"Sprzedano {sprzedanych_sztuk} sztuk produktu {sprzedawany_produkt} za {cena_sprzedawanego_prod} zl")
                produkt_sprzedany = True
            elif (prod.get("sztuk") - sprzedanych_sztuk) <= 0:
                sztuk = prod["sztuk"]
                print(f"Niestety nie mamy tylu sztuk w magazynie. Liczba dostępnych sztuk: {sztuk}")
        else:
            continue
    if produkt_sprzedany == False:
        print("Nie mamy takiego produktu")


@manager.assign("zakup")
def zakup(manager):
    kupowany_produkt = input("Podaj nazwę produktu: ")
    cena_kupowanego_prod = float(input("Podaj cenę produktu: "))
    sztuk_kupowanego_prod = int(input("Podaj liczbę sztuk: "))
    produkt_w_magazynie = False
    for produkt in manager.stan_magazynu:
        if produkt.get(
                "nazwa_produktu") == kupowany_produkt and cena_kupowanego_prod * sztuk_kupowanego_prod <= manager.saldo:
            produkt_w_magazynie = True
            produkt["sztuk"] = produkt["sztuk"] + sztuk_kupowanego_prod
            manager.saldo = manager.saldo - (cena_kupowanego_prod * sztuk_kupowanego_prod)
            manager.przeglad.append(
                f"Kupiono {sztuk_kupowanego_prod} sztuk produktu {kupowany_produkt} za {cena_kupowanego_prod} zl")
            break
        else:
            continue
    if not produkt_w_magazynie and cena_kupowanego_prod * sztuk_kupowanego_prod <= manager.saldo:
        manager.stan_magazynu.append({
            "nazwa_produktu": kupowany_produkt,
            "cena": cena_kupowanego_prod,
            "sztuk": sztuk_kupowanego_prod
        })
        manager.przeglad.append(
            f"Kupiono {sztuk_kupowanego_prod} sztuk produktu {kupowany_produkt} za {cena_kupowanego_prod} zl")
        manager.saldo = manager.saldo - (cena_kupowanego_prod * sztuk_kupowanego_prod)
    elif (cena_kupowanego_prod * sztuk_kupowanego_prod) > manager.saldo:
        print("Nie masz wystarczających środków na koncie na taki zakup.")


@manager.assign("konto")
def konto(manager):
    print(f"Stan sklepowego konta wynosi: {manager.saldo}")


@manager.assign("lista")
def lista(manager):
    for produkt in manager.stan_magazynu:
        print(f"Oto aktualny stan magazynu \n{produkt}")


@manager.assign("magazyn")
def magazyn(manager):
    produkt = input("Podaj nazwę produktu dla którego chcesz wyświetlić informacje: ")
    produkt_index = 0
    for prod in manager.stan_magazynu:
        if prod.get("nazwa_produktu") == produkt:
            print(manager.stan_magazynu[produkt_index])
            break
        else:
            produkt_index += 1
            continue


@manager.assign("przeglad")
def przeglad(manager):
    od = (input("Podaj zakres. Od którego indeksu chcesz wyświetlić przegląd?: "))
    do = (input("Do którego?: "))
    indexy = len(manager.przeglad)
    if od == "" or do == "":
        print(manager.przeglad)
    elif (int(od) > indexy or int(od) < 0) or int(do) > indexy:
        print(f"Wprowadziłeś zakres spoza listy. Liczba zapisanych akcji wynosi {indexy}")
    else:
        print(manager.przeglad[int(od):int(do)])


@manager.assign("koniec")
def koniec(manager):
    print("zakończono program")
    manager.instancja_file_handlera.zapis_do_plikow_balance_warehouse(budzet=str(manager.saldo), stan_magazynu=manager.stan_magazynu)
    manager.instancja_file_handlera.zapis_historii(historia=manager.przeglad)

koniec = False

while not koniec:
    print("dostępne komendy:\n - saldo\n- sprzedaz\n- zakup\n- konto\n- lista\n- magazyn\n- przeglad\n- koniec")
    komenda = input("Wprowadź odpowiednią komendę: ")

    if komenda == "saldo":
        manager.execute("saldo")
    elif komenda == "sprzedaz":
        manager.execute("sprzedaz")
    elif komenda == "zakup":
        manager.execute("zakup")
    elif komenda == "konto":
        manager.execute("konto")
    elif komenda == "lista":
        manager.execute("lista")
    elif komenda == "magazyn":
        manager.execute("magazyn")
    elif komenda == "przeglad":
        manager.execute("przeglad")
    elif komenda == "koniec":
        manager.execute("koniec")
        koniec = True
