kysymys_1 = "mikä on veden kemiallinen merkki? 1. H2O 2. CO2 3. O2"
oikea_vastaus1 = "1"
kysymys_2 = "Mikä on Italian pääkaupunki? 1. Milano 2. Rooma 3. Venetsia"
oikea_vastaus2 = "2"
kysymys_3 = "Mikä on maailman pisin joki? 1. Amazonas 2. Niili 3. Mississippi"
oikea_vastaus3 = "3"
laskuri = 0
print("--QUIZ GAME--")
print("[1] Aloita peli")
print("[2] Ohjeet")
print("[3] Lopeta")
syote = input("1, 2, 3: ")

if syote == "2":
    print("--OHJEET--")
    print("Vastaa kysymyksiin oikein, jokaisesta oikeasta vastauksesta saat vaikeustason verran pisteitä!")
    print("Kun sinulla on 30000 pistettä, voitat pelin.")
    syote = input("Valitse nyt 1 (Aloita peli) tai 3 (Lopeta): ")
if syote == "3":
    print("Kiitos pelistä! Hei hei!")
    exit()
 
if syote == "1":
    taso = 1
    laskuri = 0
    print("Peli alkaa!")


while laskuri < 30000:
    if taso == 1:
        nykyinen_kysymys = kysymys_1
        oikea_vastaus = oikea_vastaus1
        pistelisays = 500
    elif taso == 2:
        nykyinen_kysymys = kysymys_2
        oikea_vastaus = oikea_vastaus2
        pistelisays = 2500
    else:
        nykyinen_kysymys = kysymys_3
        oikea_vastaus = oikea_vastaus3
        pistelisays = 5000

    print(nykyinen_kysymys)
    pelaajan_vastaus = input("Anna vastaus: ")
    if pelaajan_vastaus == oikea_vastaus:
        print(f"Sait {pistelisays} pistettä!")
        laskuri += pistelisays
        print(f"Pisteet: {laskuri}")
        taso += 1
    else:
        print("Väärin meni!")
        break
                
    if laskuri >= 30000:
        print("Voitit pelin! Pisteet yhteensä", laskuri)
        
else:
    syote = input("Virheellinen valinta, valitse: 1, 2 tai 3: ")

