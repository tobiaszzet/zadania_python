print("Gra w kółko i krzyżyk. Komputer rozpoczyna grę.")

pole1 = "-"
pole2 = "-"
pole3 = "-"
pole4 = "-"
pole5 = "X"
pole6 = "-"
pole7 = "-"
pole8 = "-"
pole9 = "-"

computer_win = False
draw = False
print(f"{pole1, pole2, pole3}\n{pole4, pole5, pole6} \n{pole7, pole8,pole9}")

while pole1 == "-" or pole2 == "-" or pole3 == "-" or pole4 == "-" or pole6 == "-" or pole7 == "-"or pole8 == "-"or pole9 == "-":
    kolko = input("wprowadź numer pustego pola: ")

    if kolko == "1" and pole1 == "-":
        pole1 = "o"
    elif kolko == "2" and pole2 == "-":
        pole2 = "o"
    elif kolko == "3" and pole3 == "-":
        pole3 = "o"
    elif kolko == "4" and pole4 == "-":
        pole4 = "o"
    elif kolko == "6" and pole6 == "-":
        pole6 = "o"
    elif kolko == "7" and pole7 == "-":
        pole7 = "o"
    elif kolko == "8" and pole8 == "-":
        pole8 = "o"
    elif kolko == "9" and pole9 == "-":
        pole9 = "o"
    else:
        print("Błąd")
        continue

    if pole1 == "o"  and pole2 == "o" and pole3 == "-":
        pole3 = "X"
    elif pole1 == "-"  and pole2 == "o" and pole3 == "o":
        pole1 = "X"
    elif pole1 == "o"  and pole2 == "-" and pole3 == "o":
        pole2 = "X"

    elif pole3 == "o"  and pole6 == "o" and pole9 == "-":
        pole9 = "X"
    elif pole3 == "o"  and pole6 == "-" and pole9 == "o":
        pole6 = "X"
    elif pole3 == "-"  and pole6 == "o" and pole9 == "o":
        pole3 = "X"

    elif pole7 == "o" and pole8 == "o" and pole9 == "-":
        pole9 = "X"
    elif pole7 == "o" and pole8 == "-" and pole9 == "o":
        pole8 = "X"
    elif pole7 == "-" and pole8 == "o" and pole9 == "o":
        pole7 = "X"

    elif pole1 == "o"  and pole4 == "o" and pole7 == "-":
        pole7 = "X"
    elif pole1 == "-"  and pole4 == "o" and pole7 == "o":
        pole1 = "X"
    elif pole1 == "o"  and pole4 == "-" and pole7 == "o":
        pole4 = "X"

    elif pole1 == "o" and pole7 == "-":
        pole7 = "X"
    elif pole3 == "o" and pole9 == "-":
        pole9 = "X"
    elif pole9 == "o" and pole7 == "-":
        pole7 = "X"
    elif pole7 == "o" and pole1 == "-":
        pole1 = "X"

    elif pole2 == "o" and pole1 == "-":
        pole1 = "X"
    elif pole6 == "o" and pole3 == "-":
        pole3 = "X"
    elif pole8 == "o" and pole9 == "-":
        pole9 = "X"
    elif pole4 == "o" and pole4 == "-":
        pole7 = "X"

    elif pole1 == "X" and pole9 == "-":
        pole9 = "X"
    elif pole2 == "X" and pole8 == "-":
        pole8 = "X"
    elif pole3 == "o" and pole7 == "-":
        pole7 = "X"

    elif pole4 == "X" and pole6 == "-":
        pole6 = "6"
    elif pole6 == "X" and pole4 == "-":
        pole4 = "X"

    elif pole7 == "X" and pole3 == "-":
        pole3 = "X"
    elif pole8 == "X" and pole2 == "-":
        pole2 = "X"
    elif pole9 == "X" and pole1 == "-":
        pole1 = "X"

    else:
        if pole3 == "-":
            pole3 = "X"
        elif pole6 == "-":
            pole6 = "X"
        elif pole4 == "-":
            pole4 = "X"
        elif pole1 == "-":
            pole1 = "X"
        elif pole9 == "-":
            pole9 = "X"
        elif pole8 == "-":
            pole8 = "X"
        elif pole7 == "-":
            pole7 = "X"
        elif pole2 == "-":
            pole2 = "X"

    print(f"{pole1, pole2, pole3}\n{pole4, pole5, pole6} \n{pole7, pole8, pole9}")

    if pole1 == "X" and pole2 == "X" and pole3 == "X":
        computer_win = True
        break
    elif pole4 == "X" and pole5 == "X" and pole6 == "X":
        computer_win = True
        break
    elif pole7 == "X" and pole8 == "X" and pole9 == "X":
        computer_win = True
        break
    elif pole1 == "X" and pole4 == "X" and pole7 == "X":
        computer_win = True
        break
    elif pole2 == "X" and pole5 == "X" and pole8 == "X":
        computer_win = True
        break
    elif pole3 == "X" and pole6 == "X" and pole9 == "X":
        computer_win = True
        break
    elif pole1 == "X" and pole5 == "X" and pole9 == "X":
        computer_win = True
        break
    elif pole3 == "X" and pole5 == "X" and pole7 == "X":
        computer_win = True
        break


if not computer_win:
    draw = True
    print(f"\n  R E M I S")
else:
    print(f"\n  KOMPUTER W Y G R A Ł")

