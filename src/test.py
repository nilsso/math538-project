from melody import melody_to_seqs

# A sample melody
melody = [
        'c,4,4',
        'g,3,2',
        'c,4,4'
        ]

# Converted to numerical sequences
pitch_seq, rhythm_seq = melody_to_seqs(melody)

print(pitch_seq)
print(rhythm_seq)
