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
    # Unconventionally this operator now returns a tuple of the absolute pitch
    # difference and the rhythm difference
    def __sub__(self, other):
        pitch_diff = abs((self.octave-other.octave)*12+(self.deg-other.deg))
        rhythm_diff = abs(self.value-other.value)
        return pitch_diff, rhythm_diff

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
    a = ([Note.parse(note) for note in vals])
    a, b = a[1:], a[:-1]
    a, b = map(list, zip(*[b[i]-a[i] for i in range(len(a))]))
    return a, b
