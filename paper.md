---
header-includes:
   \usepackage{amsmath, amssymb, xfrac}
---
<!--
present a 20-25 minutes slide or power point presentation that will be judged by
the rest of the class, the instructor and other faculty members that will attend
the presentations.

The teams must also submit a formal project (very much in the style of a journal
publication). The report should not exceed 20 pages (including all graphic
material) and should include:
- Title, authors, affiliations.
- Abstract.
- Introductory background material on the literature and significance of the
  project.
- Development of the mathematical model or a survey of a collection of relevant
  models.
- Discussion on the relevant mathematical theory that applies.
- Some original work on your own for either extending the model and performing
  simulations.
- Discussion and conclusions to summarize your work.
- References.

-->

# Abstract

Music and mathematics are two subjects more related to one-another than most
people know. A single melody can be thought of as a sequence of changing pitch
frequency intervals, along side a sequence of rhythmic durations. In this
project we will first explore ways in which to translate musical melodies into
real-valued numerical sequences, and second we will study these sequences by
applying familiar fractal dimension metrics in an attempt to explore fractal
patterns in music and build insight into what "fractal music" really means.

---

<!-- "Introduction"? -->
<!-- SECTION ------------------------------------------------------------- -->

# Fractals

# Fractals in music

## Misconceptions

<!-- SECTION ------------------------------------------------------------- -->
# A primer on music

## Pitch, notes, rhythm

## Intervals and melody

<!-- SECTION ------------------------------------------------------------- -->
# Self-similarity scaling in music 

One of the earliest attempts at mathematically quantifying musical
self-similarity was conducted by Richard Voss and John Clarke. From their
results they concluded that within genres of music a $\sfrac 1 f$ power-law
scaling behavior is characteristic of musical components for pieces in the genre
(though they were specifically concerned with the Baroque era compositions of
J.S. Bach, or just "classical" in layman's terms).
<!-- -->
However, there may be many different ways in which measurable self-similarity
within music can manifest; chapter 7 of the Mandelbrot text, written by
Brothers, provides a few examples of how scaling within music has been
quantified:

1. *Duration scaling*: the distribution of durations for individual notes is
   self-similar within a piece,
2. *Pitch scaling*: the distribution of pitches is statistically self-similar,
3. *Melodic interval scaling*: the distribution of melodic intervals is
   self-similar,
4. *Melodic moment scaling*: the distribution of the changes in melodic
   intervals is stylistically self-similar,
5. *Harmonic interval scaling*: the distribution of harmonic intervals is
   self-similar,
6. *Structural scaling*: the structure of the music from a compositional
   standpoint relies on nested or recursive patterns, and
7. *Motivic scaling*: a motif, melodic or rhythmic, is repeated simultaneously
   at different time scales (called augmentation or diminution).

<!-- SECTION ------------------------------------------------------------- -->

# Fractal and multifractal dimension

<!-- SECTION ------------------------------------------------------------- -->
# Structural scaling and motivic scaling: Bach and fractals

The first part of the fifth movement, the "Bourrée", from
Johann Sebastian Bach's Cello Suite No. 3 in C Major, BWV 1009.

The paper <PAPER> by <AUTHORS> is dedicated entirely to examining the scaling
characteristics within this single section of music, and the paper "Multifractal
analyses of music sequences" by Zhi-Yuan Su and Tzuyin Wu also takes a look at
this very same section (along with two other musical examples).

![Cello Suite No. 3 in C Major, BWV 1009, V. Bourrée I.](./music/bwv1009_bourree.png)

<!-- SECTION ------------------------------------------------------------- -->
# Pitch scaling: Stochastic composition

- Describe the procedure used to compose Guapos and Nils
- Analyze Guapos and Nils
- Expand on what pitch scaling is
- Describe how Guapos and Nils provides an example of pitch scaling fracticality

A  | B  | C  | Total | Note
-- | -- | -- | --    | --
2  | 6  | 1  | 9     | C
2  | 6  | 5  | 13    | G
2  | 2  | 5  | 9     | C
2  | 6  | 2  | 10    | D
4  | 6  | 2  | 12    | F
1  | 6  | 3  | 10    | D
2  | 4  | 3  | 9     | C
6  | 2  | 1  | 9     | C

<!-- SECTION ------------------------------------------------------------- -->
# Melodic interval and duration scaling: implementing

## Converting a melodic line into point sequences

## Limitations of the method

The most dramatic limitation of this procedure is that it requires the musical
material to be monophonic---only one note at a time---while the vast majority of
modern music (and actually the majority of music since the 14th century) is
polyphonic. Despite this, a piece of music containing simultaneous notes across
simultaneous voices could potentially be reconstructed into standalone parts,
where each roughly functions as standalone piece consisting of only a monophonic
melody. Think of a Bach cantata for soprano, alto, tenor and bass four-part
choir, where each voice is essentially its own piece, its own melody. On the
other hand, not all music can be so simply reconstructed into parts. Even the
Bach selection examined by Su and Wu (the Bourrée), despite being almost
entirely monophonic, contains polyphony in measures 2, 4, and 28 (the last), but
this may be an artifact of the editor, as some copies have a single G instead of
the E chord. Either way, one can simplify a polyphonic melody by selecting a
single constituent note whenever there's a simultaneous group of notes, as I did
for simplifying the Bourrée.

![French Suite No. 5 in G Major, BWV 1009, III. Gavotte](./music/bwv816_gavotte.png)


