import sys
from pprint import pprint
from services.luo_opetusdata_abc import LuoOpetusData
from entities.trierakenne import TrieRakenne


def main(savellaji, nuotit):
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
    opetusdata = TrieRakenne()
    x = 0
    for i in data.opetusdata_muunnettu:
        try: 
            #print(f"Ensimmäinen: {data.opetusdata_muunnettu[x]} Toinen: {data.opetusdata_muunnettu[x+1]} Kolmas: {data.opetusdata_muunnettu[x+2]}")
            opetusdata.lisaa_nuotit([data.opetusdata_muunnettu[x], data.opetusdata_muunnettu[x+1], data.opetusdata_muunnettu[x+2]])
        except IndexError:
            #print(f"Ensimmäinen: {data.opetusdata_muunnettu[x]} Toinen: G kolmas: G")
            opetusdata.lisaa_nuotit([data.opetusdata_muunnettu[x], "18", "18"])

        x+=1
    #opetusdata.lisaa_nuotit(data.opetusdata_muunnettu)
    #print(TrieRakenne.etsi_nuotit(opetusdata, "19"))
    print(TrieRakenne.maarita_painokertoimet(nuotit, opetusdata))


if __name__ == "__main__":
    savellaji = "G"
    nuotit = ["18", "19"]
    main(savellaji, nuotit)