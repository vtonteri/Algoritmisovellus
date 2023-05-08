import random
from services.luo_opetusdata_abc import LuoOpetusData
from services.opi_opetusdatasta import OpiDatasta
from services.tee_uusi_midi_tiedosto import TeeUusiMidiTiedosto
from entities.trierakenne import TrieRakenne

class LuoUusiKappale():

    def __init__(self, savellaji, tilojen_maara, nuotit, oktaavi):
        self.data = LuoOpetusData()
        self.data.lue_ja_muunna_abc_data(savellaji)
        self.opetusdata = OpiDatasta()
        self.tilojen_maara = tilojen_maara
        self.opittu_data = self.opetusdata.opi(self.tilojen_maara, self.data.opetusdata_muunnettu)
        self.nuotit = nuotit
        self.savellaji = savellaji
        self.uusi_kappale = []
        self.savelet_abc_notaationa = []
        self.apulista_2 = []
        self.oktaavi = oktaavi

    def luo_uusi_kappale(self):
        for i in range(100):
            seuraavat_mahdolliset_nuotit = TrieRakenne.maarita_painokertoimet(self.nuotit, self.opittu_data, self.savellaji)
            vertailu_kerroin = random.random()
            for nuotti, painokerroin in seuraavat_mahdolliset_nuotit.items():
                if vertailu_kerroin <= painokerroin:
                    self.uusi_kappale.append(nuotti)
                    break

            if len(self.nuotit) < self.tilojen_maara-1:
                self.nuotit.append(nuotti)
            
            elif len(self.nuotit) == self.tilojen_maara-1:
                self.nuotit.pop(0)
                self.nuotit.append(nuotti)


        self.savelet_abc_notaationa = LuoOpetusData().lue_ja_muunna_savel_data(self.uusi_kappale)
        uusi_midi = TeeUusiMidiTiedosto(self.oktaavi, 0, self.savellaji, self.tilojen_maara)
        uusi_midi.luo_uusi_midi_tiedosto(self.savelet_abc_notaationa)
