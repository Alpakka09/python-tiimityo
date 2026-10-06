import random

class kysymys:
    def __init__(self, teksti, vaihto_a, vaihto_b, vaihto_c, oikea_vastaus, vaikeustaso):
        self.teksti = teksti
        self.vaihtoehdot = [vaihto_a, vaihto_b, vaihto_c]
        self.oikea_vastaus = int(oikea_vastaus)
        self.vaikeustaso = int(vaikeustaso)

    def tarkista_vastaus(self, pelaajan_vastaus):
        return int(pelaajan_vastaus) == self.oikea_vastaus
    
#Tällä funktiolla luetaan tiedosto ja rakennetaan tiedolla oliota.
def lue_kysymykset(tiedostonimi):

    kysymyslista = [] #Valmiit kysymykset lisätään tänne.

    with open(tiedostonimi, "r", encoding ="utf-8") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.strip()
            if not rivi: #Ohitetaan kaikki mahdolliset tyhjät rivit tiedoston lopussa.
                continue

            osat = rivi.split("|")

            if len(osat) == 6:
                uusi_kysymys = kysymys(osat[0], osat[1], osat[2], osat[3], osat[4], osat[5])

                kysymyslista.append(uusi_kysymys)

    return kysymyslista

def arvo_kysymys(kysymyslista, vaikeustaso):
    # Tällä funktiolla suodatetaaan vain halutun vaikeustason kysymykset listasta
    sopivat_kysymykset = []
    for kysymys in kysymyslista:
        if kysymys.vaikeustaso == vaikeustaso:
            sopivat_kysymykset.append(kysymys)

    if not sopivat_kysymykset:
        return None

    return random.choice(sopivat_kysymykset)

def tallenna_tulos(nimi, pisteet, tiedostonimi="tulokset.csv"):
    #Tällä funktiolla voi tallentaa pelaajan tulokset tulokset.csv tiedostoon.  
    with open(tiedostonimi, "a", encoding="utf-8") as tiedosto:
        tiedosto.write(f"{nimi},{pisteet}\n")

if __name__ == "__main__":
    ladatut_kysymykset = lue_kysymykset("kysymykset.txt")
    print(f"Ladattiin onnistuneesti {len(ladatut_kysymykset)} kysymystä!")

    # Testi arpoo tällä komennolla ensimmäisen vaikeusasteen kysymyksen
    arvottu = arvo_kysymys(ladatut_kysymykset, 1)

    if arvottu:
        print(f"\nArvottiin satunnainen tason 1 kysymys:")
        print(f"Kysymys: {arvottu.teksti}")
        print(f"Vaihtoehdot: {arvottu.vaihtoehdot}")

    print("\nTestataan tuloksen tallennusta...")
    tallenna_tulos("Testipelaaja", 500)
    print("Tulos tallennettu! Voit käydä katsomassa tulokset.csv -tiedostoa.")