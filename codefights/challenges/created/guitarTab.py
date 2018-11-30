description = """%
You have a guitar-playing friend
You will convert C-4 E-4 G#4 etc. to a guitar tab

https://en.wikipedia.org/wiki/ASCII_tab


|Fret|E|A|D|G|B|e|
|--|--|--|--|--|--|--|
|0|E2|A2|D3|G3|B3|E4|
|1|F2|A#2|D#3|G#3|C4|F4|
|2|F#2|B2|E3|A3|C#4|F#4|
|3|G2|C3|F3|A#3|D4|G4|
|4|G#2|C#3|F#3|B3|D#4|G#4|
|5|A2|D3|G3|C4|E4|A4|
|6|A#2|D#3|G#3|C#4|F4|A#4|
|7|B2|E3|A3|D4|F#4|B4|
|8|C3|F3|A#3|D#4|G4|C5|
|9|C#3|F#3|B3|E4|G#4|C#5|
|A(10)|D3|G3|C4|F4|A4|D5|
|B(11)|D#3|G#3|C#4|F#4|A#4|D#5|
|C(12)|E3|A3|D4|G4|B4|E5|
|D(13)|F3|A#3|D#4|G#4|C5|F5|
|E(14)|F#3|B3|E4|A4|C#5|F#5|
|F(15)|G3|C4|F4|A#4|D5|G5|


Standard Guitar Tuning

e 0 (E-4)
  1  F-4
  2  F#4
  3  G-4
  4  G#4
  5  A-4
  6  A#4
  7  B-4
  8  C-4
  9  C#4
  
B (B-3)
G (G-3)
D (D-3)
A (A-2)
E (E-2)

(thickest string on bottom)

E-2 <= notes <= C#4

e -3-9- = G-4, C#5
B -----
G -----
D -----
A -----
E -0--- = E-2


equivalent note
...
A -0-1-...
E -5-6-...

...
B -0-
G -4-
...
"""

range = ['E-2',  # string E
         'F-2',
         'F#2',
         'G-2',
         'G#2',  
         'A-2',  # string A
         'A#2',
         'B-2',
         "C-3",
         "C#3",
         "D-3",  # string D
         "D#3",
         'E-3',
         'F-3',
         'F#3',
         'G-3',  # string G
         'G#3',
         'A-3',
         'A#3',
         'B-3',  # string B
         "C-4",
         "C#4",
         "D-4",
         "D#4",
         'E-4',  # string e
         'F-4',
         'F#4',
         'G-4',
         'G#4',
         'A-4',
         'A#4',
         'B-4',
         'C-5',
         'C#5']

strings = [
    ['E-4',  # string e
     'F-4',
     'F#4',
     'G-4',
     'G#4',
     'A-4',
     'A#4',
     'B-4',
     'C-5',
     'C#5'],

    ['B-3',  # string B
     "C-4",
     "C#4",
     "D-4",
     "D#4",],

    ['G-3',  # string G
     'G#3',
     'A-3',
     'A#3',],
        
    ["D-3",  # string D
     "D#3",
     'E-3',
     'F-3',
     'F#3',],

    ['A-2',  # string A
     'A#2',
     'B-2',
     "C-3",
     "C#3",],

    ['E-2',  # string E
     'F-2',
     'F#2',
     'G-2',
     'G#2',],
]

