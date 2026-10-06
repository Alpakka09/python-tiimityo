import logiikka
kysymykset = logiikka.lue_kysymykset("kysymykset.txt")
laskuri = 0
taso = 1
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
else:
    syote = input("Virheellinen valinta, valitse: 1, 2 tai 3: ")


while laskuri < 23000:
    peli = logiikka.arvo_kysymys(kysymykset, taso)
    if taso == 1:
        pistelisays = 500
    elif taso == 2:
        pistelisays = 2500
    else:
        pistelisays = 5000

    if peli is None:
        print("Kysymystä ei löytynyt.")
        break
    print(peli.teksti)

    for numero, vaihtoehto in enumerate(peli.vaihtoehdot, 1):
        print(f"{numero}. {vaihtoehto}")
    pelaajan_vastaus = input("Anna vastaus: ")

    if pelaajan_vastaus not in ["1", "2", "3"]:
        print("Valitse vaihtoehto 1, 2 tai 3!")
        continue

    if peli.tarkista_vastaus(pelaajan_vastaus):
        print(f"Sait {pistelisays} pistettä!")
        laskuri += pistelisays
        print(f"Pisteet: {laskuri}")
        if taso < 3:
            taso += 1
    else:
        print("Väärin meni!")
        nimi = input("Anna nimesi: ")
        logiikka.tallenna_tulos(nimi, laskuri)
        break
                    
    if laskuri >= 30000:
        print("Voitit pelin! Pisteet yhteensä", laskuri)
        nimi = input("Anna nimesi voittajien listalle: ")
        logiikka.tallenna_tulos(nimi, laskuri)

