import unittest
from src.entities.trierakenne import TrieRakenne, TrieSolmu

class TestTrierakenne(unittest.TestCase):
    
    def setUp(self):
        self.testi_trierakenne = TrieRakenne()
        self.lisattavat_nuotit_1 = [1, 2, 3, 4, 5, 6]
        self.lisattavat_nuotit_2 = [1, 2, 3, 5, 6, 2]
        self.lisattavat_nuotit_3 = [1, 2, 3, 6, 2, 3]
        self.etsittavat_nuotit = ["1", "2", "3"]
        self.testi_rakenne = TrieSolmu()
        self.testi_rakenne.lapsi = {4:TrieSolmu()}
        self.testi_rakenne.maara = 1
        self.testi_rakenne.on_viimeinen = False

    def test_lisaa_nuotit(self):
        self.assertEqual(self.testi_trierakenne.lisaa_nuotit(self.lisattavat_nuotit_1), True)

    def test_etsi_nuotit(self):
        self.testi_trierakenne.lisaa_nuotit(self.lisattavat_nuotit_1)
        self.assertEqual(self.testi_trierakenne.etsi_nuotit(["1", "2", "3"]).lapsi.keys(), self.testi_rakenne.lapsi.keys())
        self.assertEqual(self.testi_trierakenne.etsi_nuotit(["1", "2", "3"]).maara, self.testi_rakenne.maara)
        self.assertEqual(self.testi_trierakenne.etsi_nuotit(["1", "2", "3"]).on_viimeinen, self.testi_rakenne.on_viimeinen)

    def test_maarita_painokertoimet(self):
        self.testi_trierakenne.lisaa_nuotit(self.lisattavat_nuotit_1)
        self.testi_trierakenne.lisaa_nuotit(self.lisattavat_nuotit_2)
        self.testi_trierakenne.lisaa_nuotit(self.lisattavat_nuotit_3)

        self.assertEqual(TrieRakenne.maarita_painokertoimet(["1", "2", "3"], self.testi_trierakenne, "G"), {4: 0.3333333333333333, 5: 0.6666666666666666, 6: 1.0})