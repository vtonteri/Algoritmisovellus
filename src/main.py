import sys
from pprint import pprint
from services.luo_opetusdata_abc import LuoOpetusData
from entities.trierakenne import TrieRakenne


def main():
    """
    Tavoiteltava lopputulos:
        
        Ajaa algoritmin seuraavasti: 
        1. lukee opetusdatan /data/opetusdata -kansiosta käyttäen lue_opetusdata -metodia
        2. luo opetusdatan käyttäen services -> luo_opetusdata -metodia
        3. luo Trie-rakenteen opetusdatan perusteella
        4. luo uuden kappaleen Trie-rakenteen perusteella /data/tulosdata-kansioon
    
    6.4.2023 toiminta:
        1. Lukee opetusdatan (tällä hetkellä vain yhden tiedoston (G_data_1.txt)) 
        2. Luo opetusdatan (muuntaa tiedoston nuotit numeroiksi ja tekee listan)
        3. Luo opetusdatan pohjalta Trie-rakenteen
    
    nuotit = "kala"
    liaa = "mies"
    f = "kalamies"
    s = "mieskala"
    t = "kalakala"
    y = "kalatyyppi"
    x = TrieRakenne()

    x.lisaa_nuotit(nuotit)
    x.lisaa_nuotit(liaa)
    x.lisaa_nuotit(f)
    x.lisaa_nuotit(s)
    x.lisaa_nuotit(t)
    x.lisaa_nuotit(y)
    x.lisaa_nuotit(y)
    x.lisaa_nuotit(y)
    x.lisaa_nuotit(y)
    x.lisaa_nuotit(["j","a","r"])
    print(TrieRakenne.maarita_painokertoimet(["k", "a", "l", "a"], x))
    """
    
    data = LuoOpetusData()
    data.lue_ja_muunna_abc_data()
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
    print(TrieRakenne.maarita_painokertoimet(["19", "18", "17"], opetusdata))


if __name__ == "__main__":
    main()