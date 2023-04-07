tinklelis = [" " for i in range(9)]

def tinklelio_eiles():
    eile_1 = f"| {tinklelis[0]} | {tinklelis[1]} | {tinklelis[2]} |"
    eile_2 = f"| {tinklelis[3]} | {tinklelis[4]} | {tinklelis[5]} |"
    eile_3 = f"| {tinklelis[6]} | {tinklelis[7]} | {tinklelis[8]} |"
    print("Kryziukai - Nuliukai")
    print(eile_1)
    print(eile_2)
    print(eile_3)
    print("--------------------")

def zaidejas(simbolis):
    if simbolis == "X":
        numeris = 1
    elif simbolis == "O":
        numeris = 2

    print(f"{numeris}-ojo zaidejo ejimas:")

    vieta = int(input("Iveskite pasirinkta vieta (nuo 1 iki 9): ").strip())
    if tinklelis[vieta - 1] == " ":
        tinklelis[vieta - 1] = simbolis
    else:
        print()
        print("Sita vieta uzimta!")

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
        print("Laimejo draugyste!")
        break
    zaidejas("O")
    if laimejimas("O"):
        tinklelio_eiles()
        print("Zaidejas O laimejo!")
        break
    elif lygiosios():
        print("Laimejo draugyste!")
        break