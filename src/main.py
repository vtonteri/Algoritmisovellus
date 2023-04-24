from services.luo_opetusdata_abc import LuoOpetusData
from services.luo_uusi_kappale import LuoUusiKappale
import os


def main(savellaji, nuotit, tilojen_maara):
    """
    Tavoiteltava lopputulos:
        
        Ajaa algoritmin seuraavasti: 
        1. lukee opetusdatan /data/opetusdata -kansiosta käyttäen lue_opetusdata -metodia
        2. luo opetusdatan käyttäen services -> luo_opetusdata -metodia
        3. luo Trie-rakenteen opetusdatan perusteella
        4. luo uuden kappaleen Trie-rakenteen perusteella /data/tulosdata-kansioon
    
    23.4.2023 toiminta:
        1. Lukee valitusta opetusdatakansiosta kaikkien tiedostojen sisällön
        2. Luo opetusdatan (muuntaa tiedoston nuotit numeroiksi ja tekee listan)
        3. Luo opetusdatan pohjalta Trie-rakenteen
        4. Määrittää Trie-rakenteesta painokertoimet ja palauttaa dict:n, mikä sisältää seuraavien nuottien painokertoimet
    """
    LuoUusiKappale(savellaji, tilojen_maara, nuotit).luo_uusi_kappale()

    


if __name__ == "__main__":

    """
    savellaji -muuttuja määrittää mistä opetusdata -kansion kansiosta opetusdata luetaan
    nuotit - listalla määritetään mikä nuottikierto etsitään luodusta trie-rakenteesta
    tilojen_maara -muuttujalla määritetään, kuinka monta tasoa luodaan opetusdataan (Trie-rakenne). 
    nuotit -listan alkioiden määrän tulee olla yksi vähemmän kuin tilojen määrä
    """
    
    try: 
        tiedosto_polku =  "..\data\opetusdata"
        tiedostot_ja_kansiot = os.listdir(tiedosto_polku)
    except FileNotFoundError:
        pass
    try:
        tiedosto_polku = "data/opetusdata"
        tiedostot_ja_kansiot = os.listdir(tiedosto_polku)
    except FileNotFoundError:
        print("Ei löydetty tiedostoa, lisää opetusdataa kansioon tai vaihda sävellajia")
    
    kansiot = [f for f in tiedostot_ja_kansiot if os.path.isdir(os.path.join(tiedosto_polku, f))]

    while(True):
        savellaji = input(f"Anna sävellaji, tällä hetkellä jokin seuraavista {kansiot}. Painamalla x ohjelma lopettaa \n")
        
        if savellaji in kansiot:
            tilojen_maara = int(input(f"Anna ennustamiseen käytettävien Markovin ketjujen tilojen määrä:\n"))
            savellaji_muunnettu = LuoOpetusData().muunnos_abc_numeroksi[savellaji]
            nuotit = [savellaji_muunnettu for i in range(tilojen_maara-1)]
            main(savellaji, nuotit, tilojen_maara)
            break
        elif savellaji == "X" or savellaji == "x":
            break
        else:
            print("Anna kelvollinen sävellaji tai tilojen määrä (kokonaisluku)")