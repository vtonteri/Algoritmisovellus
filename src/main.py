import os
from services.luo_opetusdata_abc import LuoOpetusData
from services.luo_uusi_kappale import LuoUusiKappale

def main(kappaleen_savellaji, aloittavat_nuotit, markov_tilojen_maara, kappaleen_oktaavi):

    LuoUusiKappale(kappaleen_savellaji, markov_tilojen_maara, aloittavat_nuotit, kappaleen_oktaavi).luo_uusi_kappale()

if __name__ == "__main__":
    """ savellaji -muuttuja määrittää mistä opetusdata -kansion kansiosta opetusdata luetaan
        nuotit - listalla määritetään mikä nuottikierto etsitään luodusta trie-rakenteesta
        tilojen_maara -muuttujalla määritetään, kuinka monta tasoa luodaan opetusdataan (Trie-rakenne). 
        nuotit -listan alkioiden määrän tulee olla yksi vähemmän kuin tilojen määrä"""
    try:
        TIEDOSTO_POLKU =  r"..\data\opetusdata"
        TIEDOSTOT_JA_KANSIOT = os.listdir(TIEDOSTO_POLKU)
    except FileNotFoundError:
        pass
    try:
        TIEDOSTO_POLKU = r"data/opetusdata"
        TIEDOSTOT_JA_KANSIOT = os.listdir(TIEDOSTO_POLKU)
    except FileNotFoundError:
        print("Ei löydetty tiedostoa, lisää opetusdataa kansioon tai vaihda sävellajia")
    kansiot = [f for f in TIEDOSTOT_JA_KANSIOT if os.path.isdir(os.path.join(TIEDOSTO_POLKU, f))]
    MIDIN_OKTAAVI = 3

    while(True):
        savellaji = input(f"Anna sävellaji, tällä hetkellä jokin seuraavista {kansiot}. Painamalla x ohjelma lopettaa \n")
        if savellaji in kansiot:
            while True:
                tilojen_maara = input("Anna ennustamiseen käytettävien Markovin ketjujen tilojen määrä (2-6) tai x, jolloin voit vaihtaa sävellajia:\n")
                try:
                    if tilojen_maara in ("X", "x"):
                        print("Kappaletta ei luotu, seuraavaksi voit valita sävellajin uudelleen")
                        break
                    if 2 <= int(tilojen_maara) <= 6:
                        savellaji_muunnettu = LuoOpetusData().muunnos_abc_numeroksi[savellaji]
                        nuotit = [savellaji_muunnettu]
                        main(savellaji, nuotit, int(tilojen_maara), MIDIN_OKTAAVI)
                        break

                except:
                    print("Anna kelvollinen tilojen määrä")
        elif savellaji in ("X", "x"):
            print("Ohjelma lopetetaan, uutta kappaletta ei luotu.")
            break
        else:
            print("Anna kelvollinen sävellaji tai tilojen määrä (kokonaisluku väliltä 2 - 6)")
