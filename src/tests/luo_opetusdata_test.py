import unittest
from src.services.luo_opetusdata_abc import LuoOpetusData
import os

class TestLuoOpetusData(unittest.TestCase):
    
    def setUp(self):
        self.test_muunnos_abc_numeroksi = {"C,": 0, "D,": 1, "E,": 2, "F,": 3, "G,": 4, "A,": 5, "B,": 6, "C": 7, "D": 8, "E": 9, "F": 10, "G": 11, "A":12, "B": 13, "c": 14, "d": 15, "e": 16, 
                                      "f": 17, "g": 18, "a": 19, "b": 20, "c'":21, "d'": 22, "e'": 23, "f'": 24, "g'": 25, "a'": 26, "b'": 27}
        self.test_opetusdata_muunnettu = []
        self.test_muunnettu_savel_data = []

        self.muunnettu_testi_data = ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'g', 'e', 'g', 'e', 'd', 'g', 'e', 'd', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'c', 'd', 'g', 'c', 'd', 'g', 'c', 'd', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'g', 'e', 'g', 'e', 'd', 'g', 'e', 'd', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'c', 'd', 'g', 'c', 'd', 'g', 'c', 'd', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'g', 'e', 'g', 'e', 'd', 'g', 'e', 'd', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'c', 'd', 'g', 'c', 'd', 'g', 'c', 'd', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'g', 'e', 'g', 'e', 'd', 'g', 'e', 'd', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'c', 'd', 'g', 'c', 'd', 'g', 'c', 'd']
        self.testi_data_numeroina = [19, 19, 20, 20, 14, 14, 15, 15, 18, 16, 18, 16, 15, 18, 16, 15, 19, 19, 20, 20, 14, 14, 15, 15, 14, 15, 18, 14, 15, 18, 14, 15, 19, 19, 20, 20, 14, 14, 15, 15, 18, 16, 18, 16, 15, 18, 16, 15, 19, 19, 20, 20, 14, 14, 15, 15, 14, 15, 18, 14, 15, 18, 14, 15, 19, 19, 20, 20, 14, 14, 15, 15, 18, 16, 18, 16, 15, 18, 16, 15, 19, 19, 20, 20, 14, 14, 15, 15, 14, 15, 18, 14, 15, 18, 14, 15, 19, 19, 20, 20, 14, 14, 15, 15, 18, 16, 18, 16, 15, 18, 16, 15, 19, 19, 20, 20, 14, 14, 15, 15, 14, 15, 18, 14, 15, 18, 14, 15]
        self.test_luo_opetusdata = LuoOpetusData()

        
    def test_lue_ja_muunna_opetusdata(self):
        self.test_luo_opetusdata.lue_ja_muunna_abc_testi_data()

        self.assertTrue(len(self.test_luo_opetusdata.opetusdata_muunnettu) == len(self.muunnettu_testi_data))
        self.assertTrue([a == b for a, b in zip(self.test_luo_opetusdata.opetusdata_muunnettu, self.muunnettu_testi_data)])

    def test_lue_ja_muunna_savel_data(self):
        self.assertEqual(self.test_luo_opetusdata.lue_ja_muunna_savel_data(self.testi_data_numeroina), self.muunnettu_testi_data)
