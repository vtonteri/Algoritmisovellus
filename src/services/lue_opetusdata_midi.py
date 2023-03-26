from mido import MidiFile

midi = MidiFile("opetusdata\Buffalo_Springfield_-_For_What_Its_Worth.mid")

for message in midi:
    if message.type == "note_on":
        print(message)