description = """%
You have a guitar-playing friend
You will convert C-4 E-4 G#4 etc. to a guitar tab

https://en.wikipedia.org/wiki/ASCII_tab

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

