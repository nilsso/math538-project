import numpy as np
import matplotlib as mplt
from matplotlib import pyplot as plt

from melody import melody_to_seqs

# A sample melody
melody = [
        'c,4,4',
        'g,3,2',
        'c,4,4',
        'g,3,2',
        'c,4,4',
        'g,3,2',
        'c,4,4',
        'g,3,2',
        'c,4,4',
        'g,3,2',
        ]

# Converted to numerical sequences
pitch_seq, rhythm_seq = melody_to_seqs(melody)

# print(pitch_seq)
# print(rhythm_seq)

# print(pitch_seq)
plt.scatter(pitch_seq,    np.ones(len(pitch_seq)))
plt.scatter(rhythm_seq, 2*np.ones(len(pitch_seq)))
plt.show()
