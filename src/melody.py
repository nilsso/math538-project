import re

note_name_pattern = re.compile('(\w)([sf]*)')
note_pattern = re.compile('([a-zA-Z]+),(\d+),(\d+)')

note_degree = {
            'c'  : 0,
            'd'  : 2,
            'e'  : 4,
            'f'  : 5,
            'g'  : 7,
            'a'  : 9,
            'b'  : 11,
        }

def parse_note_name(token):
    m = note_name_pattern.match(token)
    assert(m)
    n, accidentals = m.groups()
    assert((len(set(accidentals)) <= 1))
    mod = 0 if not accidentals else 1 if accidentals[0] == 's' else -1
    return note_degree[n], mod*len(accidentals)

class Note:
    def __init__(self, name, deg_base, deg_shift, octave, value):
        self.name = name
        self.deg_base = deg_base
        self.deg_shift = deg_shift
        self.deg = (deg_base + deg_shift) % 12
        self.octave = octave
        self.value = value

    def __str__(self):
        return '{},{},{}'.format(self.deg, self.octave, self.value)

    def __eq__(self, other):
        assert(type(other) is Note)
        return self.deg == other.deg and self.octave == other.octave

    def __lt__(self, other):
        assert(type(other) is Note)
        return self.octave < other.octave or self.deg < other.deg

    def __gt__(self, other):
        return self.octave > other.octave or self.deg > other.deg

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def __sub__(self, other):
        return (self.octave - other.octave) * 12 + (self.deg - other.deg)

    def parse(token):
        m = note_pattern.match(token)
        assert(m is not None)
        name, octave, value = m.groups()
        deg_base, deg_shift = parse_note_name(name)
        return Note(name, deg_base, deg_shift, int(octave), int(value))

melody = [
        'c,4,4',
        'g,3,4',
        'c,4,4'
        ]

def melody_to_seq(vals):
    a = [Note.parse(note) for note in vals]
    a, b = a[1:], a[:-1]
    return [ abs(b[i]-a[i]) for i in range(len(a)) ]

print(melody_to_seq(melody))

# print(a)
# print(b)
# print(a - b)
