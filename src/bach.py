import mido

messages = mido.MidiFile('music/bwv1009_bourree.mid')
notes = [n for n in messages if type(n) is mido.Message]

for n in notes:
    print(n)
