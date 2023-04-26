from mido import MidiFile, MidiTrack, Message
from random import randint
import os


class TeeUusiMidiTiedosto:
    def __init__(self):
        self.muunnokset = {"C": 12, "c": 13, "D": 14, "d": 15, "E": 16, "F": 17, "f": 18, "G": 19, "g": 20, "A": 21, "a": 22, "B": 23, "e": 16, "b": 23}

    def luo_uusi_midi_tiedosto(self, savelet):

        mid = MidiFile()

        track = MidiTrack()
        mid.tracks.append(track)

        aika = 0

        for i in savelet:
            track.append(Message("note_on", channel = randint(5,15), note=self.muunnokset[i], velocity=127, time = aika*500))
            aika += 1

        mid.save("musaa.mid")

"""
    
            mid.save("data/tulosdata/musaa1.mid")
        except:
            pass
        try: 
            mid.save("..\data\tulosdata\musaa.mid")
        except:
            print("Ei voitu tallentaa tiedostoa.")
"""


        #for message in mid:
        #    print(message)
