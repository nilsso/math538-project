import numpy as np
import re

# NOTE: Currently not handling dotted rhythms
LY_PATTERN = re.compile(r"([a-z])(es|is)?([,'])*(\d*)")

DEGREE_MAP = {
        'c' : 0, 'd' : 2, 'e' : 4,
        'f' : 5, 'g' : 7, 'a' : 9, 'b' : 11 }

DEGREE_MAP_INV = {
        0: 'C',  1: 'C#', 2: 'D',   3: 'D#',
        4: 'E',  5: 'F',  6: 'F#',  7: 'G',
        8: 'G#', 9: 'A', 10: 'A#', 11: 'B' }

ACCIDENTAL_MAP = {
        'es': -1,
        'is': 1,
        None: 0 }

VALUE_MAP_INV = {
        1: 'whole-note',
        2: 'half-note',
        4: 'quarter-note',
        8: 'eighth-note',
        16: 'sixteenth-note' }

#! Note abstraction
class Note:
    def __init__(self, d, o, v):
        self.degree = d
        self.octave = o
        self.value = v

    @property
    def d(self):
        return self.degree

    @property
    def o(self):
        return self.octave

    @property
    def v(self):
        return self.value

    #! Subtraction operator overload
    # Returns the absolute pitch difference between notes
    def __sub__(self, other):
        degree_delta = self.d - other.d
        octave_delta = self.o - other.o
        return abs(degree_delta + octave_delta * 12)

    def __str__(self):
        return f'{DEGREE_MAP_INV[self.d]}{self.o} {VALUE_MAP_INV[self.v]}'

#! Helper to get octave of note relative to another
# @param d  Degree of note
# @param pd Degree of previous note
# @param po Octave of previous note
def relative_octave(d, pd, po):
    delta = (12 + d - pd) % 12
    # Increment if moving across C
    if pd + delta > 11:
        po += 1
    # Invert if distance is a P5 or bigger
    if delta > 6:
        po -= 1
    return po

#! Helper to get octave shift from comma/apostrophe string
# It's down/up an octave for however many commas/apostrophes.
# If empty or None, returns 0.
# @param o Comma/apostrophe string
def octave_shift(o):
    assert(o is None or len(set(o)) <= 1) # Don't mix commas and apostrophes!
    return ((-1)*len(o) if o[0] is ',' else len(o)) if o else 0

#! Melody abstraction
class Melody:
    #! Constructor
    def __init__(self, notes=None):
        self.notes = []
        if notes:
            for n in notes:
                self.addly(n)

    #! Add note (LilyPond relative octave notation)
    def addly(self, s):
        # note, accidental, octave, value:
        n, a, o, v = LY_PATTERN.match(s).groups()
        d = DEGREE_MAP[n] + ACCIDENTAL_MAP[a]

        # If first note in melody have to establish relative first note:
        if len(self.notes) == 0:
            assert(v is not None)
            o = 4 + octave_shift(o)
            self.notes += [Note(d, o, int(v))]

        # Else octave comes from previous note
        else:
            prev = self.notes[-1]
            pd, po, pv = prev.d, prev.o, prev.v
            o = relative_octave(d, pd, po) + octave_shift(o)
            v = int(v) if v else pv
            self.notes += [Note(d, o, v)]
        # print(s, ':', str(self.notes[-1]))

#! Get sequence of absolute pitch differences in melody
# @param M Melody object
def pitch_intervals(M):
    assert(type(M) is Melody)
    n = len(M.notes)-1
    res = np.zeros(n, dtype=int)
    for i in range(1, n):
        res[i] = res[i-1] + (M.notes[i] - M.notes[i-1] + 1)
    return res

#! Get sequence of rhythmic value intervals in melody
# "A shortest measure of time is first selected and a black point is marked on
# the first position of the line." The temporal interval of a note is then the
# number of times this smallest value divides the note's rhythmic value.
# @param M Melody object
def rhythmic_intervals(M):
    assert(type(M) is Melody)
    n = len(M.notes)-1
    smallest_value = max(M.notes, key=lambda n: n.v).v
    res = np.zeros(n, dtype=int)
    for i in range(1, n):
        res[i] = res[i-1] + (smallest_value // M.notes[i].v)
    return res
