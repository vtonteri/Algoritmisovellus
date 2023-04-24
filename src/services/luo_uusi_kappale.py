from services.luo_opetusdata_abc import LuoOpetusData
from services.opi_opetusdatasta import OpiDatasta
from entities.trierakenne import TrieRakenne
import random


class LuoUusiKappale():

    def __init__(self, savellaji, tilojen_maara, nuotit):
        self.data = LuoOpetusData()
        self.data.lue_ja_muunna_abc_data(savellaji)
        self.opetusdata = OpiDatasta()
        self.opittu_data = self.opetusdata.opi(tilojen_maara, self.data.opetusdata_muunnettu)
        self.nuotit = nuotit
        self.savellaji = savellaji
        self.uusi_kappale = []
        self.apulista = []
        self.apulista_2 = []

    def luo_uusi_kappale(self):

        etsittavat_nuotit = [nuotti for nuotti in self.nuotit]

        for i in range(50):
            seuraavat_mahdolliset_nuotit = TrieRakenne.maarita_painokertoimet(etsittavat_nuotit, self.opittu_data, self.savellaji)
            vertailu_kerroin = random.random()
            for nuotti, painokerroin in seuraavat_mahdolliset_nuotit.items():
                    if vertailu_kerroin <= painokerroin:
                         self.uusi_kappale.append(nuotti)
                         break
            etsittavat_nuotit.pop(0)
            etsittavat_nuotit.append(nuotti)


        x = LuoOpetusData().lue_ja_muunna_savel_data(self.uusi_kappale)
        y = 0
        for i in x:
            self.apulista_2.append(i)
            if y % 8 == 0:
                print(self.apulista_2)
                self.apulista_2 = []
            
            y += 1