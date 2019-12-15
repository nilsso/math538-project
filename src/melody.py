import numpy as np
import re

note_name_pattern = re.compile('(\w)([sf]*)')
note_pattern = re.compile('([a-zA-Z]+),(\d+),(\d+)')

# Note degree look-up table
note_degree = {
            'c'  : 0,
            'd'  : 2,
            'e'  : 4,
            'f'  : 5,
            'g'  : 7,
            'a'  : 9,
            'b'  : 11,
        }

#! Note name parser helper
def parse_note_name(token):
    m = note_name_pattern.match(token)
    assert(m)
    n, accidentals = m.groups()
    assert((len(set(accidentals)) <= 1))
    mod = 0 if not accidentals else 1 if accidentals[0] == 's' else -1
    return note_degree[n], mod*len(accidentals)

#! Note class
# For a brief description of the member fields:
# - "name" is the full name of the note (e.g. cs for C-sharp)
# - "deg_base" is the degree of the note without accidentals
# - "deg_shift" is the semitone difference from the accidentals
# - "deg" is the "deg_base" plus the "deg_shift" (a.k.a the enharmonic degree)
# - "octave" is the octave of the enharmonic degree
# - "value" is the rhythmic value of the note (1 for whole, 4 for quarter, etc.)
class Note:
    #! Standard constructor
    def __init__(self, name, deg_base, deg_shift, octave, value):
        self.name = name
        self.deg_base = deg_base
        self.deg_shift = deg_shift
        self.deg = (deg_base + deg_shift) % 12
        self.octave = octave
        self.value = value

    def __str__(self):
        return '{},{},{}'.format(self.deg, self.octave, self.value)

    #! Subtraction operator
    def __sub__(self, other):
        return abs((self.octave-other.octave)*12+(self.deg-other.deg))

    #! Parse a note string
    # The format is '<note name>,<octave>,<rhythmic value>'
    # See header comments for more.
    def parse(token):
        m = note_pattern.match(token)
        assert(m is not None)
        name, octave, value = m.groups()
        deg_base, deg_shift = parse_note_name(name)
        return Note(name, deg_base, deg_shift, int(octave), int(value))

#! Convert melody to sequences
# Converts a sequence of note strings to a sequence of absolute pitch
# differences and rhythm differences.
def melody_to_seqs(vals):
    notes = ([Note.parse(note) for note in vals])
    # Couple of constants
    n = len(notes)-1
    M = max(notes, key=lambda n: n.value).value
    # Construct pitch sequence
    pitch_seq = np.zeros(len(notes)-1, dtype=int)
    for i in range(1, len(notes)-1):
        pitch_seq[i] = notes[i]-notes[i-1]+pitch_seq[i-1]
    # Construct rhythm sequence
    rhythm_seq = pitch_seq.copy()
    for i in range(1, len(notes)-1):
        rhythm_seq[i] = rhythm_seq[i-1] + notes[i].value // M
    return pitch_seq, rhythm_seq
