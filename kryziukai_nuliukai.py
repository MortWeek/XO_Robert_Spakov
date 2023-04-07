tinklelis = [" " for i in range(9)]

def tinklelio_eiles():
    eile_1 = f"| {'1' if tinklelis[0] == ' ' else tinklelis[0]} | {'2' if tinklelis[1] == ' ' else tinklelis[1]} | {'3' if tinklelis[2] == ' ' else tinklelis[2]} |"
    eile_2 = f"| {'4' if tinklelis[3] == ' ' else tinklelis[3]} | {'5' if tinklelis[4] == ' ' else tinklelis[4]} | {'6' if tinklelis[5] == ' ' else tinklelis[5]} |"
    eile_3 = f"| {'7' if tinklelis[6] == ' ' else tinklelis[6]} | {'8' if tinklelis[7] == ' ' else tinklelis[7]} | {'9' if tinklelis[8] == ' ' else tinklelis[8]} |"
    print("Kryžiukai - Nuliukai")
    print("--------------------")
    print(eile_1)
    print(eile_2)
    print(eile_3)
    print("--------------------")

def zaidejas(simbolis):
    if simbolis == "X":
        numeris = "X"
    elif simbolis == "O":
        numeris = "O"
    print(f"{numeris}-ojo zaidejo ejimas:")

    while True:
        try:
            vieta = int(input("Iveskite pasirinkta vieta (nuo 1 iki 9): ").strip())
            if 1 <= vieta <= 9:
                if tinklelis[vieta - 1] == " ":
                    tinklelis[vieta - 1] = simbolis
                    break
                else:
                    print()
                    print("Si vieta uzimta!")
                    print(f"{numeris}-ojo zaidejo ejimas:")
            else:
                print()
                print("Ivesta netinkama reiksme!")
                print(f"{numeris}-ojo zaidejo ejimas:")
        except ValueError:
            print()
            print("Ivesta netinkama reiksme!")
            print(f"{numeris}-ojo zaidejo ejimas:")
            continue

def laimejimas(simbolis):
    if (tinklelis[0] == simbolis and tinklelis[1] == simbolis and tinklelis[2] == simbolis) or \
        (tinklelis[3] == simbolis and tinklelis[4] == simbolis and tinklelis[5] == simbolis) or \
        (tinklelis[6] == simbolis and tinklelis[7] == simbolis and tinklelis[8] == simbolis) or \
        (tinklelis[0] == simbolis and tinklelis[3] == simbolis and tinklelis[6] == simbolis) or \
        (tinklelis[1] == simbolis and tinklelis[4] == simbolis and tinklelis[7] == simbolis) or \
        (tinklelis[2] == simbolis and tinklelis[5] == simbolis and tinklelis[8] == simbolis) or \
        (tinklelis[0] == simbolis and tinklelis[4] == simbolis and tinklelis[8] == simbolis) or \
        (tinklelis[2] == simbolis and tinklelis[4] == simbolis and tinklelis[6] == simbolis):
        return True
    else:
        return False

def lygiosios():
    if " " not in tinklelis:
        return True
    else:
        return False

while True:
    tinklelio_eiles()
    zaidejas("X")
    tinklelio_eiles()
    if laimejimas("X"):
        print("Zaidejas X laimejo!")
        break
    elif lygiosios():
        print("Lygiosios!")
        break
    zaidejas("O")
    if laimejimas("O"):
        tinklelio_eiles()
        print("Zaidejas O laimejo!")
        break
    elif lygiosios():
        print("Lygiosios!")
        break