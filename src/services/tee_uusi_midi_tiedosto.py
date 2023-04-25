from mido import MidiFile, MidiTrack, Message
from random import randint


class TeeUusiMidiTiedosto:
    def __init__(self):
        pass

    def luo_uusi_midi_tiedosto(self, savelet):

        mid = MidiFile()

        track = MidiTrack()
        mid.tracks.append(track)

        for i in range(100):
            track.append(Message("note_on", channel = randint(5,15), note=randint(60,80), velocity=127, time = i*100))

        mid.save("data/tulosdata/musaa.mid")

        for message in mid:
            print(message)
