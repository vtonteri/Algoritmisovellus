from mido import MidiFile, MidiTrack, Message
from random import randint
import os


class TeeUusiMidiTiedosto:
    def __init__(self, oktaavi):
        self.mid = MidiFile(type=0)
        self.track = MidiTrack()
        self.oktaavi = oktaavi
        self.muunnokset_0 = {"C": 12, "c": 13, "D": 14, "d": 15, "E": 16, "F": 17, "f": 18, "G": 19, "g": 20, "A": 21, "a": 22, "B": 23, "e": 16, "b": 23}
        self.muunnokset_1 = {"C": 24, "c": 25, "D": 26, "d": 27, "E": 28, "e": 28, "F":	29, "f": 30, "G": 31, "g": 32, "A":	33, "a": 34, "B": 35, "b": 35}
        self.muunnokset_2 = {"C": 36, "c": 37, "D": 38, "d": 39, "E": 40, "e": 40, "F":	41, "f": 42, "G": 43, "g": 44, "A":	45, "a": 46, "B": 47, "b": 47}
        self.muunnokset_3 = {"C": 48, "c": 49, "D": 50, "d": 51, "E": 52, "e": 52, "F":	53, "f": 54, "G": 55, "g": 56, "A":	57, "a": 58, "B": 59, "b": 59}
        self.muunnokset_4 = {"C": 60, "c": 61, "D": 62, "d": 63, "E": 64, "e": 64, "F":	65, "f": 66, "G": 67, "g": 68, "A":	69, "a": 70, "B": 71, "b": 71}
        self.muunnokset_5 = {"C": 72, "c": 73, "D": 74, "d": 75, "E": 76, "e": 76, "F":	77, "f": 78, "G": 79, "g": 80, "A":	81, "a": 82, "B": 83, "b": 83}
        self.sakeisto_nuotit = []
        self.kertosae_nuotit = []
        self.melodia_nuotit = []
        self.bridge_nuotit = []
        self.aika = 256
        self.nopeus = 12

    def luo_uusi_midi_tiedosto(self, savelet):

        self.mid.tracks.append(self.track)
        indeksi = 0

        for nuotti in savelet:
            if indeksi <= 7:
                self.sakeisto_nuotit.append(nuotti)
                indeksi += 1
            elif indeksi > 7 and indeksi <= 15:
                self.kertosae_nuotit.append(nuotti)
                indeksi += 1
            elif indeksi > 15 and indeksi <= 23:
                self.melodia_nuotit.append(nuotti)
                indeksi += 1
            elif indeksi > 23 and indeksi <= 31:
                self.bridge_nuotit.append(nuotti)
                indeksi += 1

        self.sakeisto()
        self.kertosae()
        self.bridge()
        self.sakeisto()
        self.kertosae()
        self.bridge()
        self.melodia()
        self.kertosae()
        self.kertosae()

        self.mid.save("uusi_kappale.mid")

    def sakeisto(self):
        for nuotti in self.sakeisto_nuotit:
            if self.oktaavi == 0:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_0[nuotti], velocity=self.nopeus, time = self.aika))
            elif self.oktaavi == 1:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_1[nuotti], velocity=self.nopeus, time = self.aika))
            elif self.oktaavi == 2:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_2[nuotti], velocity=self.nopeus, time = self.aika))
            elif self.oktaavi == 3:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_3[nuotti], velocity=self.nopeus, time = self.aika))
            elif self.oktaavi == 4:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_4[nuotti], velocity=self.nopeus, time = self.aika))
            elif self.oktaavi == 5:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_5[nuotti], velocity=self.nopeus, time = self.aika))
    
    def kertosae(self):
        for nuotti in self.kertosae_nuotit:
            if self.oktaavi == 0:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_0[nuotti], velocity=self.nopeus, time = self.aika))
            elif self.oktaavi == 1:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_1[nuotti], velocity=self.nopeus, time = self.aika))
            elif self.oktaavi == 2:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_2[nuotti], velocity=self.nopeus, time = self.aika))
            elif self.oktaavi == 3:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_3[nuotti], velocity=self.nopeus, time = self.aika))
            elif self.oktaavi == 4:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_4[nuotti], velocity=self.nopeus, time = self.aika))
            elif self.oktaavi == 5:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_5[nuotti], velocity=self.nopeus, time = self.aika))

    def bridge(self):
        for nuotti in self.bridge_nuotit:
            if self.oktaavi == 0:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_0[nuotti], velocity=self.nopeus, time = self.aika))
            elif self.oktaavi == 1:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_1[nuotti], velocity=self.nopeus, time = self.aika))
            elif self.oktaavi == 2:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_2[nuotti], velocity=self.nopeus, time = self.aika))
            elif self.oktaavi == 3:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_3[nuotti], velocity=self.nopeus, time = self.aika))
            elif self.oktaavi == 4:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_4[nuotti], velocity=self.nopeus, time = self.aika))
            elif self.oktaavi == 5:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_5[nuotti], velocity=self.nopeus, time = self.aika))

    def melodia(self):
        for nuotti in self.melodia_nuotit:
            if self.oktaavi == 0:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_0[nuotti], velocity=self.nopeus, time = self.aika))
            elif self.oktaavi == 1:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_1[nuotti], velocity=self.nopeus, time = self.aika))
            elif self.oktaavi == 2:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_2[nuotti], velocity=self.nopeus, time = self.aika))
            elif self.oktaavi == 3:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_3[nuotti], velocity=self.nopeus, time = self.aika))
            elif self.oktaavi == 4:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_4[nuotti], velocity=self.nopeus, time = self.aika))
            elif self.oktaavi == 5:
                self.track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset_5[nuotti], velocity=self.nopeus, time = self.aika))



"""
        try: 
            os.chdir(f"..\data\musiikki")
            tulostiedostot = os.listdir(os.getcwd())
        except OSError:
            pass
        try:
            os.chdir(f"data/musiikki")
            tulostiedostot = os.listdir(os.getcwd())
        except FileNotFoundError:
            print("Jotain meni vikaan.")

        print(tulostiedostot)

        kappaleen_numero = 0
"""

