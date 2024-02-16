# Rozpoczynamy od podanej ze standardowego wejścia liczby x (od 1 do 100).
# Jeśli x jest liczbą parzystą, to kolejny wyraz ciągu będzie obliczony jako x/2.
# W przeciwnym przypadku kolejny wyraz ciągu będzie równy 3x+1.
# W ten sam sposób obliczamy kolejne wyrazy ciągu, aż pojawi się liczba 1.
#
# Napisz program, który wypisze długość ciągu Collatza dla podanego ze standardowego wejścia x.
# X może przyjmować wartości od 1 do 100.

x = float(input("Podaj liczbę od 1 do 100: "))


dlugosc_ciagu = 0


if x > 1 and x <= 100:

    while x != 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1
        dlugosc_ciagu += 1

        print(x)

else:
    print("Liczba jest poza zakresem.")

print(f"Długość ciągu wynosi: {dlugosc_ciagu}")


