ilosc_przedmiotow_do_wyslania = int(input("Podaj liczbę produktów do wysłania: "))

produkt = 1
waga_ogol = 0
liczba_paczek = 1
suma_pustych_kg = 0
najwiekszy_pusty_kg = 0
nr_paczki_z_naj_pustym_kg = 1
puste_kg_w_paczce = 20

while produkt < ilosc_przedmiotow_do_wyslania +1:
    input_wagi = float(input(f"Wprowadź wagę {produkt} przedmiotu (między 1 a 10 kg): "))

    if input_wagi < 1 or input_wagi > 10:
        print("Produkt jest poza wagą. Program przerwany")
        if waga_ogol == 0:
            liczba_paczek = 0
            nr_paczki_z_naj_pustym_kg = 0
        else:
            if puste_kg_w_paczce >= najwiekszy_pusty_kg:
                najwiekszy_pusty_kg = puste_kg_w_paczce
                nr_paczki_z_naj_pustym_kg = liczba_paczek
            suma_pustych_kg += puste_kg_w_paczce
        break

    waga_ogol += input_wagi

    if (puste_kg_w_paczce - input_wagi >= 0):
        puste_kg_w_paczce -= input_wagi
    else:
        if puste_kg_w_paczce >= najwiekszy_pusty_kg:
            najwiekszy_pusty_kg = puste_kg_w_paczce
            nr_paczki_z_naj_pustym_kg = liczba_paczek
        liczba_paczek += 1
        suma_pustych_kg += puste_kg_w_paczce
        puste_kg_w_paczce = 20 - input_wagi

    if produkt == ilosc_przedmiotow_do_wyslania and (puste_kg_w_paczce >= najwiekszy_pusty_kg):
        najwiekszy_pusty_kg = puste_kg_w_paczce
        nr_paczki_z_naj_pustym_kg = liczba_paczek
        suma_pustych_kg += puste_kg_w_paczce

    produkt += 1


print(f"Wysłano {liczba_paczek} paczki")
print(f"Wysłano {waga_ogol} kg")
print(f"Suma pustych kilogramów {suma_pustych_kg}")
print(f"Najwięcej pustych kg ma paczka {nr_paczki_z_naj_pustym_kg} ({najwiekszy_pusty_kg}kg)")
