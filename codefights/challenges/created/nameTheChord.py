description = """

You have carefully built an Arduino frequency analyzer and its first test will be taking apart [triad chords](https://en.wikipedia.org/wiki/Chord_(music)#Triads).

The Arduino reports the three frequencies (in Hertz) of the triad chord as an array. It will be the input to your function, whose output should be the root note, from A to G, followed by the conventional symbol for the *quality* of the chord:

| Quality | Symbol |
|--|--|
|major|*none*|
|minor|m|
|augmented|aug|
|diminished|dim|


"""

description2 = """

You have carefully built an Arduino frequency analyzer and its first test will be taking apart [triad chords](https://en.wikipedia.org/wiki/Chord_(music)#Triads) and deducing which chord was played.

The Arduino reports the three frequencies (in Hertz) of the triad chord as an array. 

This array of three floats will be the input to your function, whose output should be the root note, from A to G (the octave is ignored), followed by the conventional symbol for the *quality* of the chord:

| Quality | Symbol |
|--|--|
|major|*none*|
|minor|m|
|augmented|aug|
|diminished|dim|

All notes were played in [twelve-tone equal temperament](https://en.wikipedia.org/wiki/Equal_temperament) with A4 (the note "La" above middle C or "Do") equal to `440 Hz`.

"""

description3 =
"""

You have carefully built an Arduino frequency analyzer and its first test will be taking apart [triad chords](https://en.wikipedia.org/wiki/Chord_(music)#Triads) and deducing which chord was played.

The Arduino reports the three frequencies (in Hertz) of the triad chord as an array. 

This array of three floats will be the input to your function, whose output should be the root note, from A to G (the octave is ignored), followed by the conventional symbol for the *quality* of the chord. The distances (in semitones) of the two notes above the root are given below:

| Quality | Symbol | Semitones above root |
|--|--|--|
|major|*- none -*|4, 7|
|minor|m|3, 7|
|augmented|aug|4, 8|
|diminished|dim|3, 6|

All notes were played in [twelve-tone equal temperament](https://en.wikipedia.org/wiki/Equal_temperament) with A4 (the note "La" above middle C or "Do") equal to `440 Hz`.

"""
