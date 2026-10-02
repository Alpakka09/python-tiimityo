kysymys = "mikä on veden kemiallinen merkki? 1. H2O 2. CO2 3. O2"
oikea_vastaus = "1"
laskuri = 0

while True:
    print("--QUIZ GAME--")
    print("[1] Aloita peli")
    print("[2] Ohjeet")
    print("[3] Lopeta")
    syote = input("1, 2, 3: ")
    
    if syote == "1":
        print("Valitse vaikeustaso:")
        print("[1] Helppo (500 pistettä)")
        print("[2] Keskivaikea (750 pistettä)")
        print("[3] Vaikea (1000 pistettä)")
        taso = input("1, 2, 3: ")
        if taso == "1":
            piste_lisays = 500
            print("Valitsit helpon tason, saat 500 pistettä!")
        elif taso == "2":
            piste_lisays = 750
            print("Valitsit keskivaikean tason, saat 750 pistettä!")
        else:
            piste_lisays = 1000
            print("Valitsit vaikean tason, saat 1000 pistettä!")
        while laskuri < 10000:
            print(kysymys)
            pelaajan_vastaus = input("Anna vastaus: ")
            if pelaajan_vastaus == oikea_vastaus:
                print(f"Sait {piste_lisays} pistettä!")
                laskuri += piste_lisays
                print(f"Pisteet: {laskuri}")
            else:
                print("Väärin meni!")
                break
            
            if laskuri >= 10000:
                print("Voitit pelin!")
                break
            else:
                break
            
    elif syote == "2":
        print("--OHJEET--")
        print("Vastaa kysymyksiin oikein, jokaisesta oikeasta vastauksesta saat 1000 pistettä!")
        print("Kun sinulla on 10000 pistettä, voitat pelin.")
        continue
    elif syote == "3":
        print("Kiitos pelistä! Hei hei!")
        break
    else: 
        print("Virheellinen valinta, valitse: 1, 2 tai 3")
        continue