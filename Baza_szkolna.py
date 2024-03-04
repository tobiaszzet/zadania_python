print("Witaj w programie do zarządzania bazą szkolną.")


class Uczen:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa

    def __repr__(self):
        return f"Uczeń/uczennica {self.imie} {self.nazwisko}"


class Nauczyciel:
    def __init__(self, imie, nazwisko, przedmiot, klasy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.przedmiot = przedmiot
        self.klasy = klasy

    def __repr__(self):
        return (f"Nauczyciel/ka {self.imie} {self.nazwisko},lista przedmiotów: {self.przedmiot}, lista klas: {self.klasy}")


class Wychowawca:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa

    def __repr__(self):
        return f"Wychowawcą klasy {self.klasa} jest {self.imie} {self.nazwisko}"


uczniowie = [Uczen(imie="Mateusz", nazwisko="Nowak", klasa="3c"),
         Uczen(imie="Martyna", nazwisko="Zielińska", klasa="3c")]

nauczyciele = [Nauczyciel(imie="Andrzej", nazwisko="Kowalski", przedmiot="matematyka",
                          klasy=["1a", "2a", "3c", "4b"]),
               Nauczyciel(imie="Jerzy", nazwisko="Mazur", przedmiot="j.angielski",
                          klasy=["3c","2d"])]

wychowawcy = [Wychowawca(imie="Tadeusz", nazwisko="Wiśniewski", klasa="3c")]


def znajdz_uczniow_klasy(nr_klasy):
    lista_uczniow_klasy = []

    for uczen in uczniowie:
        if uczen.klasa == nr_klasy:
            lista_uczniow_klasy.append(uczen)

    return lista_uczniow_klasy


def znajdz_wychowawce_klasy(nr_klasy):
    wychowawca_klasy = None

    for wychowawca in wychowawcy:
        if wychowawca.klasa == nr_klasy:
            wychowawca_klasy = wychowawca
    return wychowawca_klasy


def dane_nauczyciela(imie, nazwisko):
    for nauczyciel in nauczyciele:
        if nauczyciel.imie == imie and nauczyciel.nazwisko == nazwisko:
            return nauczyciel.imie, nauczyciel.nazwisko, nauczyciel.klasy


def nr_klasy_wychowawcy(imie, nazwisko):
    for wychowawca in wychowawcy:
        if wychowawca.imie == imie and wychowawca.nazwisko == nazwisko:
            return wychowawca.klasa


def klasa_ucznia(imie, nazwisko):
    for uczen in uczniowie:
        if uczen.imie == imie and uczen.nazwisko == nazwisko:
            return uczen.klasa


def lekcje_ucznia(klasa):
    lista_przedmiotow = {}
    for nauczyciel in nauczyciele:
         for klasa_nauczyciela in nauczyciel.klasy:
             if klasa_nauczyciela == klasa:
                 imie_nazwisko = nauczyciel.imie + ' ' + nauczyciel.nazwisko
                 lista_przedmiotow[nauczyciel.przedmiot] = imie_nazwisko

    return lista_przedmiotow



koniec = False

while not koniec:

    komenda = input("Dostępne komendy to: \n- utwórz \n- zarządzaj\n- koniec\n Wprowadź komendę: ")

    if komenda == "utwórz":
        koniec_utworz = False
        while not koniec_utworz:
            operacja = input("Co chcesz dodać?\n-uczeń \n-nauczyciel\n-wychowawca\n- wyjście\n: ")

            if operacja == "uczeń":
                input_imienia_ucznia = input("Wprowadź imię ucznia: ")
                input_nazwiska_ucznia = input("Wprowadź nazwisko ucznia: ")
                input_klasy_ucznia = input("Wprowadź klasę ucznia: ")
                uczniowie.append(Uczen(imie=input_imienia_ucznia, nazwisko=input_nazwiska_ucznia, klasa=input_klasy_ucznia))

            elif operacja == "nauczyciel":
                input_imienia_nauczyciela = input("Wprowadź imię nauczyciela: ")
                input_nazwiska_nauczyciela = input("Wprowadź nazwisko nauczyciela: ")
                input_przedmiot_nauczyciela = input("Wprowadź przedmiot: ")

                lista_klas = []
                brak = False
                while not brak:
                    klasa = input("Dodaj nową klasę (aby zakończyć naciśnij enter): ")
                    if klasa != "":
                        lista_klas.append(klasa)
                    else:
                        brak = True
                nauczyciele.append(Nauczyciel(imie=input_imienia_nauczyciela, nazwisko=input_nazwiska_nauczyciela,
                                              przedmiot=input_przedmiot_nauczyciela, klasy=lista_klas))

            elif operacja == "wychowawca":
                input_imienia_wychowawcy = input("Wprowadź imię wychowawcy: ")
                input_nazwiska_wychowawcy = input("Wprowadź nazwisko wychowawcy: ")
                input_klasy_wychowawcy = input("Wprowadź klasę wychowawcy: ")
                jest_wychowawca = False
                for k in wychowawcy:
                    if k.klasa == input_klasy_wychowawcy:
                        print("Ta klasa ma już wychowawcę. Wybierz inną klasę")
                        jest_wychowawca = True
                        break
                    else:
                        continue
                if not jest_wychowawca :
                    wychowawcy.append(Wychowawca(imie=input_imienia_wychowawcy,
                                                 nazwisko=input_nazwiska_wychowawcy, klasa=input_klasy_wychowawcy))

            elif operacja == "wyjście":
                break
            else:
                print("Podałeś błędną komendę")
                continue

    elif komenda == "zarządzaj":
        koniec_zarzadzaj = False

        while not koniec_zarzadzaj:
            operacja = input("Co chcesz wybrać ?\n- klasa\n- uczeń \n- nauczyciel\n- wychowawca\n- wyjście\n: ")

            if operacja == "uczeń":
                imie_ucznia = input("Wprowadź imię ucznia: ")
                nazwisko_ucznia = input("Wprowadź nazwisko ucznia: ")
                input_klasa_ucznia = klasa_ucznia(imie_ucznia, nazwisko_ucznia)
                input_lekcje_ucznia = lekcje_ucznia(input_klasa_ucznia)
                print(f"Lista lekcji ucznia {imie_ucznia, nazwisko_ucznia}:\n{input_lekcje_ucznia}")

            elif operacja == "klasa":
                nr_klasy = input("Dla której klasy chcesz wyświetlić listę uczniów?: ")
                print(f"Oto lista uczniów w klasie {nr_klasy}: \n{znajdz_uczniow_klasy(nr_klasy)}")
                print(znajdz_wychowawce_klasy(nr_klasy))

            elif operacja == "nauczyciel":
                imie_nauczyciela = input("Wprowadź imię nauczyciela: ")
                nazwisko_nauczyciela = input("Wprowadź nazwisko nauczyciela: ")
                input_dane_nauczyciela = dane_nauczyciela(imie_nauczyciela, nazwisko_nauczyciela)
                print(input_dane_nauczyciela)

            elif operacja == "wychowawca":
                imie_wychowawcy = input("Wprowadź imię wychowawcy: ")
                nazwisko_wychowawcy = input("Wprowadź nazwisko wychowawcy: ")
                klasa_wychowawcy = nr_klasy_wychowawcy(imie_wychowawcy,nazwisko_wychowawcy)
                print(f"Uczniowie tego wychowawcy to: {znajdz_uczniow_klasy(klasa_wychowawcy)}")

            elif operacja == "wyjście":
                koniec_zarzadzaj = True
            else:
                print("Podałeś błędną komendę")
                continue
    elif komenda == "koniec":
        koniec = True
    else:
        print("Podałeś błędną komendę.")
