import unittest
from src.entities.trierakenne import TrieRakenne

class TestTrierakenne(unittest.TestCase):
    
    def setUp(self):
        self.testi_trierakenne = TrieRakenne()
        self.lisattavat_nuotit_1 = ["1", "2", "3", "4", "5", "6"]
        self.lisattavat_nuotit = ["11", "12", "13", "14", "15"]
        self.lisattavat_nuotit_2 = ["15", "14", "13", "12", "11"]
        self.etsittavat_nuotit = ["1", "2", "3"]

    def test_lisaa_nuotit(self):
        self.assertEqual(self.testi_trierakenne.lisaa_nuotit(self.lisattavat_nuotit_1), True)

    def test_etsi_nuotit(self):
        self.assertEqual(self.testi_trierakenne.etsi_nuotit(["1", "2", "3"]), True)
        


    """
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