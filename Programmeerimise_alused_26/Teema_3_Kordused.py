while True:
    print("\nTee valik: ")
    print("1. while-tsükkel")
    print("2. while True ja break")
    print("3. for-tsükkel")
    print("4. summa ja keskmine")
    print("5. loendamine ja suurim")
    print("0. Välju")

    valik = input("Vali tegevus: ")
    if valik == "0":
        break
    elif valik == "1":
        #1. while-tsükkel
        x = 0
        while x < 30:
            if x % 2 == 0:
                print(x, end=" ")
            x += 1
    elif valik == "2":
        #2. while True ja break
        x = 0
        while True:
            if x % 2 == 0:
                print(x, end=" ")
            if x == 30:
                break
            x += 1
    elif valik == "3":
        #3. for-tsükkel
        for i in range(0, 31, 2):
            print(i, end=" ")
    elif valik == "4":
        #4 summa ja keskmine
        N = int(input("N: "))
        summa = 0
        i = 1
        while i <= N:
            summa = summa + i
            i = i + 1
        print("Summa:", summa)
        print("Keskmine:", summa / N)
    elif valik == "5":
        #5 loendamine ja suurim
        kogus = 0
        suurim = None
        for i in range(5):
            arv = float(input(f"{i + 1}. arv: "))
            if arv > 0:
                kogus += 1
            if suurim is None or arv > suurim:
                suurim = arv
        print("Positiivseid arve:", kogus)
        print("Suurim arv:", suurim)
    else:
        print("Vale valik!")