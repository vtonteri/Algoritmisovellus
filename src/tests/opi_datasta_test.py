import unittest
from src.entities.trierakenne import TrieRakenne, TrieSolmu
from src.services.opi_opetusdatasta import OpiDatasta

class TestOpiDatasta(unittest.TestCase):

    def setUp(self):
        self.oikea_tulos = {15: 0.42105263157894735, 18: 0.8421052631578947, 19: 1.0}
        self.testi_data_numeroina = [19, 19, 20, 20, 14, 14, 15, 15, 18, 16, 18, 16, 15, 18, 16, 15, 19, 19, 20, 20, 14, 14, 15, 15, 14, 15, 18, 14, 15, 18, 14, 15, 19, 19, 20, 20, 14, 14, 15, 15, 18, 16, 18, 16, 15, 18, 16, 15, 19, 19, 20, 20, 14, 14, 15, 15, 14, 15, 18, 14, 15, 18, 14, 15, 19, 19, 20, 20, 14, 14, 15, 15, 18, 16, 18, 16, 15, 18, 16, 15, 19, 19, 20, 20, 14, 14, 15, 15, 14, 15, 18, 14, 15, 18, 14, 15, 19, 19, 20, 20, 14, 14, 15, 15, 18, 16, 18, 16, 15, 18, 16, 15, 19, 19, 20, 20, 14, 14, 15, 15, 14, 15, 18, 14, 15, 18, 14, 15]
        self.testi_opetus_tietorakenne = OpiDatasta()

    def test_opi(self):
        self.assertEqual(self.oikea_tulos, TrieRakenne.maarita_painokertoimet(["14", "15"], self.testi_opetus_tietorakenne.opi(3, self.testi_data_numeroina), "G"))