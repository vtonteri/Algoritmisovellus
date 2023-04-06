import sys
from pprint import pprint
from services.luo_opetusdata_abc import LuoOpetusData
from entities.trierakenne import TrieRakenne


def main():
    """Tavoiteltava lopputulos:
        
        Ajaa algoritmin seuraavasti: 
        1. lukee opetusdatan /data/opetusdata -kansiosta käyttäen lue_opetusdata -metodia
        2. luo opetusdatan käyttäen services -> luo_opetusdata -metodia
        3. luo Trie-rakenteen opetusdatan perusteella
        4. luo uuden kappaleen Trie-rakenteen perusteella /data/tulosdata-kansioon"""
    
    """6.4.2023 toiminta:
    1. Lukee opetusdatan (tällä hetkellä vain ) Trie-rakenteen
    """
    data = LuoOpetusData()
    opetusdata = TrieRakenne()
    opetusdata.lisaa_nuotit(data.opetusdata_muunnettu)
    opetusdata.maarita_painokertoimet("")


    

if __name__ == "__main__":
    main()