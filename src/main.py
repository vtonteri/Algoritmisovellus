import sys
from pprint import pprint
from services.luo_opetusdata_abc import LuoOpetusData
from services.opi_opetusdatasta import OpiDatasta
from entities.trierakenne import TrieRakenne


def main(savellaji, nuotit, tilojen_maara):
    """
    Tavoiteltava lopputulos:
        
        Ajaa algoritmin seuraavasti: 
        1. lukee opetusdatan /data/opetusdata -kansiosta käyttäen lue_opetusdata -metodia
        2. luo opetusdatan käyttäen services -> luo_opetusdata -metodia
        3. luo Trie-rakenteen opetusdatan perusteella
        4. luo uuden kappaleen Trie-rakenteen perusteella /data/tulosdata-kansioon
    
    6.4.2023 toiminta:
        1. Lukee valitusta opetusdatakansiosta kaikkien tiedostojen sisällön
        2. Luo opetusdatan (muuntaa tiedoston nuotit numeroiksi ja tekee listan)
        3. Luo opetusdatan pohjalta Trie-rakenteen
        4. Määrittää Trie-rakenteesta painokertoimet ja palauttaa dict:n, mikä sisältää seuraavien nuottien painokertoimet
    """
    
    data = LuoOpetusData()
    data.lue_ja_muunna_abc_data(savellaji)
    opetusdata = OpiDatasta()
    x = opetusdata.opi(tilojen_maara, data.opetusdata_muunnettu)
    print(TrieRakenne.maarita_painokertoimet(nuotit, x))

if __name__ == "__main__":
    savellaji = "G"
    nuotit = ["18", "18"]
    tilojen_maara = 3
    main(savellaji, nuotit, tilojen_maara)