import unittest
from mido import MidiFile, MidiTrack, Message
from src.entities.trierakenne import TrieRakenne, TrieSolmu
from src.services.tee_uusi_midi_tiedosto import TeeUusiMidiTiedosto

class TestLuoMidi(unittest.TestCase):
    
    def setUp(self):
        self.testi_trierakenne = TrieRakenne()
        self.lisattavat_nuotit_1 = [1, 2, 3, 4, 5, 6]
        self.lisattavat_nuotit_2 = [1, 2, 3, 5, 6, 2]
        self.lisattavat_nuotit_3 = [1, 2, 3, 6, 2, 3]
        self.lisattavat_nuotit_4 = [1, 2]
        self.etsittavat_nuotit = ["1", "2", "3"]
        self.testi_rakenne = TrieSolmu()
        self.testi_rakenne.lapsi = {4:TrieSolmu()}
        self.testi_rakenne.maara = 1
        self.testi_rakenne.on_viimeinen = False
        

        self.muunnokset_0 = {"C": 12, "c": 13, "D": 14, "d": 15, "E": 16, "F": 17, "f": 18, "G": 19, "g": 20, "A": 21, "a": 22, "B": 23, "e": 16, "b": 23}
        self.muunnokset_1 = {"C": 24, "c": 25, "D": 26, "d": 27, "E": 28, "e": 28, "F":	29, "f": 30, "G": 31, "g": 32, "A":	33, "a": 34, "B": 35, "b": 35}
        self.muunnokset_2 = {"C": 36, "c": 37, "D": 38, "d": 39, "E": 40, "e": 40, "F":	41, "f": 42, "G": 43, "g": 44, "A":	45, "a": 46, "B": 47, "b": 47}
        self.muunnokset_3 = {"C": 48, "c": 49, "D": 50, "d": 51, "E": 52, "e": 52, "F":	53, "f": 54, "G": 55, "g": 56, "A":	57, "a": 58, "B": 59, "b": 59}
        self.muunnokset_4 = {"C": 60, "c": 61, "D": 62, "d": 63, "E": 64, "e": 64, "F":	65, "f": 66, "G": 67, "g": 68, "A":	69, "a": 70, "B": 71, "b": 71}
        self.muunnokset_5 = {"C": 72, "c": 73, "D": 74, "d": 75, "E": 76, "e": 76, "F":	77, "f": 78, "G": 79, "g": 80, "A":	81, "a": 82, "B": 83, "b": 83}

        self.muunnettu_testi_data = ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'g', 'e', 'g', 'e', 'd', 'g', 'e', 'd', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'c', 'd', 'g', 'c', 'd', 'g', 'c', 'd', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'g', 'e', 'g', 'e', 'd', 'g', 'e', 'd', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'c', 'd', 'g', 'c', 'd', 'g', 'c', 'd', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'g', 'e', 'g', 'e', 'd', 'g', 'e', 'd', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'c', 'd', 'g', 'c', 'd', 'g', 'c', 'd', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'g', 'e', 'g', 'e', 'd', 'g', 'e', 'd', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'c', 'd', 'g', 'c', 'd', 'g', 'c', 'd']
        self.testi_data_numeroina = [19, 19, 20, 20, 14, 14, 15, 15, 18, 16, 18, 16, 15, 18, 16, 15, 19, 19, 20, 20, 14, 14, 15, 15, 14, 15, 18, 14, 15, 18, 14, 15, 19, 19, 20, 20, 14, 14, 15, 15, 18, 16, 18, 16, 15, 18, 16, 15, 19, 19, 20, 20, 14, 14, 15, 15, 14, 15, 18, 14, 15, 18, 14, 15, 19, 19, 20, 20, 14, 14, 15, 15, 18, 16, 18, 16, 15, 18, 16, 15, 19, 19, 20, 20, 14, 14, 15, 15, 14, 15, 18, 14, 15, 18, 14, 15, 19, 19, 20, 20, 14, 14, 15, 15, 18, 16, 18, 16, 15, 18, 16, 15, 19, 19, 20, 20, 14, 14, 15, 15, 14, 15, 18, 14, 15, 18, 14, 15]
"""
    def test_luo_kappale_oktaavi_0(self):

        testi_midi_tuottava = TeeUusiMidiTiedosto(0, 1, "G")
        print(testi_midi_tuottava.luo_uusi_midi_tiedosto(self.muunnettu_testi_data))


    def test_luo_kappale_oktaavi_1(self):

        self.assertEqual(self.testi_trierakenne.lisaa_nuotit(self.lisattavat_nuotit_1), True)

    def test_luo_kappale_oktaavi_2(self):

        self.assertEqual(self.testi_trierakenne.lisaa_nuotit(self.lisattavat_nuotit_1), True)

    def test_luo_kappale_oktaavi_3(self):

        self.assertEqual(self.testi_trierakenne.lisaa_nuotit(self.lisattavat_nuotit_1), True)

    def test_luo_kappale_oktaavi_4(self):

        self.assertEqual(self.testi_trierakenne.lisaa_nuotit(self.lisattavat_nuotit_1), True)

    def test_luo_kappale_oktaavi_5(self):

        self.assertEqual(self.testi_trierakenne.lisaa_nuotit(self.lisattavat_nuotit_1), True)
"""