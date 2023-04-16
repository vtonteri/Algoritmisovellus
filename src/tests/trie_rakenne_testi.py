import unittest
from src.entities.trierakenne import Trierakenne

class TestTrierakenne(unittest.TestCase):
    
    def setUp(self):
        testi_trierakenne = Trierakenne()
        self.testi_opetusdata = Trierakenne()

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