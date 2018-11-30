simpleASCIIGuitarTabDescFinal = """
You're learning the guitar and wish to practice playing simple melodies. You know the notes for the melodies, so you type them in a text file. Now all that's left is some code to output an [ASCII guitar tab](https://en.wikipedia.org/wiki/ASCII_tab)!

**Note**: If you have played guitar and are familiar with music theory, please skip to the section **Your Task**.

A note is a symbol from this repeating list (we are not using flats here):

`C, C#, D, D#, E, F, F#, G, G#, A, A#, B`
 
A note is followed by the octave it belongs to (roughly, how high-pitched it is). 

The octave number increases when moving from `B` to the following `C`.

Middle C on the piano is in the fourth octave, so its symbol is `C4`.

A guitar's *standard tuning* assigns the following pitches to the six strings, starting from the thickest one (the lowest pitched one):

`E2, A2, D3, G3, B3, E4`.

In the ASCII tab you will produce, the thinnest, `E4`, string appears first, on top. To tell the two `E` strings apart, `E2` is written as a capital `E` and `E4` as a lowercase `e`.

Placing a finger on a fret will produce a sharper note when picking that string. Each fret is one **semitone** higher than the previous one. Increasing a note by one semitone is equivalent to going one note to the right on the list of twelve notes above.

Note that all intervals between strings except between G3 and B3 are 5 semitones. From G3 to B3, there are 4 semitones.

A sound made by picking a string is represented by a number written on the corresponding line of the tab. A `0` means the string is *open*, that is, you don't touch any fret. A fretted note will be correspond to how many frets away it is from the top, starting with `1`.

![C chord](https://i.imgur.com/BFtGP3C.png)
(credit: Kiefer.Wolfowitz, Wikipedia)

In the diagram above, `G4` is being played. Placing a finger on the third fret is like increasing `E4` by three semitones: `E4 > F4 > F#4 > G4`. So, we write `3` on the `e` string:

```
e |-3-|
B |---|
G |---|
D |---|
A |---|
E |---|
```


As another example, 

```
e |---|
B |---|
G |---|
D |---|
A |-0-|
E |---|
```

means you should play the note `A2` without touching the fretboard. Observe that all other strings should have a dash,`-`, in the same column of the note played.

The complete note-to-fret table you will need is shown below. Note that the fifth fret will never be used; it is shown just to highlight how the same note can appear on different strings. However, on a real guitar, the quality of a note played on different strings will sound different for various reasons (such as the variable string thicknesses).

(You may have to expand this side panel in order the see the entire table)

|Fret|E|A|D|G|B|e|
|--|--|--|--|--|--|--|
|0|E2|A2|D3|G3|B3|E4|
|1|F2|A#2|D#3|G#3|C4|F4|
|2|F#2|B2|E3|A3|C#4|F#4|
|3|G2|C3|F3|A#3|D4|G4|
|4|G#2|C#3|F#3|**B3**|D#4|G#4|
|5|**A2**|**D3**|**G3**|C4|**E4**|A4|

__Your Task__

An empty ASCII tab should look like:

```
e |-|
B |-|
G |-|
D |-|
A |-|
E |-|
```

Given a string representing a space-separated sequence of notes, output an array of six strings with the correct numbers for each note. Each element of the array is a line of the ASCII tab as shown above. 

For each note, write it on the lowest fret number possible (for example, if you have to write `B2`, write a `2` on the `A` string, not `7` on the `E` string.

Ignore the rhythm (beats and rests) of the melody. There should be exactly one dash to the column on the left and on the right of each note. 

Begin each line with the string's open note and a bar character, `|`, as shown above, and end each line with a bar character.

__Examples__

The opening measure of Metallica's "Nothing Else Matters" is `E2 G3 B3 E4 B3 G3`

You should output

```
["e |-------0-----|", 
 "B |-----0---0---|", 
 "G |---0-------0-|", 
 "D |-------------|", 
 "A |-------------|", 
 "E |-0-----------|"]
```

The beginning of "Joy to the World" is:

`D4 C#4 B3 A3`
`G3 F#3 E3 D3`

which should produce

```
["e |-----------------|", 
 "B |-3-2-0-----------|", 
 "G |-------2-0-------|", 
 "D |-----------4-2-0-|", 
 "A |-----------------|", 
 "E |-----------------|"]
```

"""


descriptionB = """
You're learning the guitar and wish to practice playing simple melodies. You know the notes for the melodies, so you type them in a text file. Now all that's left is some code to output an [ASCII guitar tab](https://en.wikipedia.org/wiki/ASCII_tab)!

**Note**: If you have played guitar and are familiar with music theory, please skip to the section **Your Task**.

A note is a symbol from this repeating list (we are not using flats here):

`C, C#, D, D#, E, F, F#, G, G#, A, A#, B`
 
A note is followed by the octave it belongs to (roughly, how high-pitched it is). 

The octave number increases when moving from `B` to the following `C`.

Middle C on the piano is in the fourth octave, so its symbol is `C4`.

A guitar's *standard tuning* assigns the following pitches to the six strings, starting from the thickest one (the lowest pitched one):

`E2, A2, D3, G3, B3, E4`.

In the ASCII tab you will produce, the thinnest, `E4`, string appears first, on top. To tell the two `E` strings apart, `E2` is written as a capital `E` and `E4` as a lowercase `e`.

Placing a finger on a fret will produce a sharper note when picking that string. Each fret is one **semitone** higher than the previous one. Increasing a note by one semitone is equivalent to going one note to the right on the list of twelve notes above.

Note that all intervals between strings except between G3 and B3 are 5 semitones. From G3 to B3, there are 4 semitones.

A sound made by picking a string is represented by a number written on the corresponding line of the tab. A `0` means the string is *open*, that is, you don't touch any fret. A fretted note will be correspond to how many frets away it is from the top, starting with `1`.

![C chord](https://i.imgur.com/BFtGP3C.png)
(credit: Kiefer.Wolfowitz, Wikipedia)

In the diagram above, `G4` is being played. Placing a finger on the third fret is like increasing `E4` by three semitones: `E4 > F4 > F#4 > G4`. So, we write `3` on the `e` string:

```
e |-3-|
B |---|
G |---|
D |---|
A |---|
E |---|
```


As another example, 

```
e |---|
B |---|
G |---|
D |---|
A |-0-|
E |---|
```

means you should play the note `A2` without touching the fretboard. Observe that all other strings should have a dash,`-`, in the same column of the note played.

The complete note-to-fret table you will need is shown below. Note that the fifth fret will never be used; it is shown just to highlight how the same note can appear on different strings. However, on a real guitar, the quality of a note played on different strings will sound different for various reasons (such as the variable string thicknesses).

(You may have to expand this side panel in order the see the entire table)

|Fret|E|A|D|G|B|e|
|--|--|--|--|--|--|--|
|0|E2|A2|D3|G3|B3|E4|
|1|F2|A#2|D#3|G#3|C4|F4|
|2|F#2|B2|E3|A3|C#4|F#4|
|3|G2|C3|F3|A#3|D4|G4|
|4|G#2|C#3|F#3|**B3**|D#4|G#4|
|5|**A2**|**D3**|**G3**|C4|**E4**|A4|

__Your Task__

An empty ASCII tab should look like:

```
e |----------|
B |----------|
G |----------|
D |----------|
A |----------|
E |----------|
```

Given a string representing a sequence of notes, output an array of six strings with the correct numbers, where each element is a line of an ASCII tab as shown above. 

Ignore the rhythm (beats and rests) of the melody. There should be exactly one dash to the column on the left and on the right of each note. 

Include the string's note and a bar character, `|`, as shown, and end each line with a bar character.

For each note, write it on the lowest fret number possible (for example, if you have to write `B2`, write a `2` on the `A` string, not `7` on the `E` string.

__Examples__

The opening measure of Metallica's "Nothing Else Matters" is `E2 G3 B3 E4 B3 G3`

You should output

```
["e |-------0-----|", 
 "B |-----0---0---|", 
 "G |---0-------0-|", 
 "D |-------------|", 
 "A |-------------|", 
 "E |-0-----------|"]
```

The beginning of "Joy to the World" is:

`D4 C#4 B3 A3`
`G3 F#3 E3 D3`

which should produce

```
["e |-----------------|", 
 "B |-3-2-0-----------|", 
 "G |-------2-0-------|", 
 "D |-----------4-2-0-|", 
 "A |-----------------|", 
 "E |-----------------|"]
```
"""



description5 = """
You're learning the guitar and wish to practice playing simple melodies. You know the notes for the melodies, so you type them in a text file. Now all that's left is some code to output an [ASCII guitar tab](https://en.wikipedia.org/wiki/ASCII_tab)!

**Note**: If you have played guitar and are familiar with music theory, please skip to the section **Your Task**.

A note is a symbol from this repeating list (we are not using flats here):

`C, C#, D, D#, E, F, F#, G, G#, A, A#, B`
 
A note is followed by the octave it belongs to (roughly, how high-pitched it is). 

The octave number increases when moving from `B` to the following `C`.

Middle C on the piano is in the fourth octave, so its symbol is `C4`.

A guitar's *standard tuning* assigns the following pitches to the six strings, starting from the thickest one (the lowest pitched one):

`E2, A2, D3, G3, B3, E4`.

In the ASCII tab you will produce, the thinnest, `E4`, string appears first, on top. To tell the two `E` strings apart, `E2` is written as a capital `E` and `E4` as a lowercase `e`.

Placing a finger on a fret will produce a sharper note when picking that string. Each fret is one **semitone** higher than the previous one. Increasing a note by one semitone is equivalent to going one note to the right on the list of twelve notes above.

Note that all intervals between strings except between G3 and B3 are 5 semitones. From G3 to B3, there are 4 semitones.

A sound made by picking a string is represented by a number written on the corresponding line of the tab. A `0` means the string is *open*, that is, you don't touch any fret. A fretted note will be correspond to how many frets away it is from the top, starting with `1`.

![C chord](https://i.imgur.com/BFtGP3C.png)
(credit: Kiefer.Wolfowitz, Wikipedia)

In the diagram above, `G4` is being played. Placing a finger on the third fret is like increasing `E4` by three semitones: `E4 > F4 > F#4 > G4`. So, we write `3` on the `e` string:

```
e |-3-|
B |---|
G |---|
D |---|
A |---|
E |---|
```


As another example, 

```
e |---|
B |---|
G |---|
D |---|
A |-0-|
E |---|
```

means you should play the note `A2` without touching the fretboard. Observe that all other strings should have a dash,`-`, in the same column of the note played.

The complete note-to-fret table you will need is shown below. Note that the fifth fret will never be used; it is shown just to highlight how the same note can appear on different strings. However, on a real guitar, the quality of a note played on different strings will sound different for various reasons (such as the variable string thicknesses).

(You may have to expand this side panel in order the see the entire table)

|Fret|E|A|D|G|B|e|
|--|--|--|--|--|--|--|
|0|E2|A2|D3|G3|B3|E4|
|1|F2|A#2|D#3|G#3|C4|F4|
|2|F#2|B2|E3|A3|C#4|F#4|
|3|G2|C3|F3|A#3|D4|G4|
|4|G#2|C#3|F#3|**B3**|D#4|G#4|
|5|**A2**|**D3**|**G3**|C4|**E4**|A4|

__Your Task__

An empty ASCII tab should look like:

```
e |----------|
B |----------|
G |----------|
D |----------|
A |----------|
E |----------|
```

Given a string representing a sequence of notes, output an array of six strings with the correct numbers, where each element is a line of an ASCII tab as shown above. 

Ignore the rhythm (beats and rests) of the melody. There should be exactly one dash to the column on the left and on the right of each note. 

Include the string's note and a bar character, `|`, as shown, and end each line with a bar character.

For each note, write it on the lowest fret number possible (for example, if you have to write `B2`, write a `2` on the `A` string, not `7` on the `E` string.

__Examples__

The opening measure of Metallica's "Nothing Else Matters" is `E2 G3 B3 E4 B3 G3`

The beginning of "Joy to the World" is:

`D4 C#4 B3 A3`
`G3 F#3 E3 D3`
"""

description4 = """
You're learning the guitar and wish to practice playing simple melodies. You know the notes for the melodies, so you type them in a text file. Now all that's left is some code to output an [ASCII guitar tab](https://en.wikipedia.org/wiki/ASCII_tab)!

**Note**: If you have played guitar and are familiar with music theory, please skip to the section **Your Task**.

A note is a symbol from this repeating list (we are not using flats here):

`C, C#, D, D#, E, F, F#, G, G#, A, A#, B`
 
A note is followed by the octave it belongs to (roughly, how high-pitched it is). 

The octave number increases when moving from `B` to the following `C`.

Middle C on the piano is in the fourth octave, so its symbol is `C4`.

A guitar's *standard tuning* assigns the following pitches to the six strings, starting from the thickest one (the lowest pitched one):

`E2, A2, D3, G3, B3, E4`.

In the ASCII tab you will produce, the thinnest, `E4`, string appears first, on top. To tell the two `E` strings apart, `E2` is written as a capital `E` and `E4` as a lowercase `e`.

Placing a finger on a fret will produce a sharper note when picking that string. Each fret is one **semitone** higher than the previous one. Increasing a note by one semitone is equivalent to going one note to the right on the list of twelve notes above.

Note that all intervals between strings except between G3 and B3 are 5 semitones. From G3 to B3, there are 4 semitones.

A sound made by picking a string is represented by a number written on the corresponding line of the tab. A `0` means the string is *open*, that is, you don't touch any fret. A fretted note will be correspond to how many frets away it is from the top, starting with `1`.

![C chord](https://i.imgur.com/BFtGP3C.png)
(credit: Kiefer.Wolfowitz, Wikipedia)

In the diagram above, `G4` is being played. Placing a finger on the third fret is like increasing `E4` by three semitones: `E4 > F4 > F#4 > G4`. So, we write `3` on the `e` string:

```
e |-3-|
B |---|
G |---|
D |---|
A |---|
E |---|
```


As another example, 

```
e |---|
B |---|
G |---|
D |---|
A |-0-|
E |---|
```

means you should play the note `A2` without touching the fretboard. Observe that all other strings should have a dash,`-`, in the same column of the note played.

The complete note-to-fret table you will need is shown below. Note that the fifth fret will never be used; it is shown just to highlight how the same note can appear on different strings. However, on a real guitar, the quality of the note will sound different because of their physical differences.

(You may have to expand this side panel in order the see the entire table)

|Fret|E|A|D|G|B|e|
|--|--|--|--|--|--|--|
|0|E2|A2|D3|G3|B3|E4|
|1|F2|A#2|D#3|G#3|C4|F4|
|2|F#2|B2|E3|A3|C#4|F#4|
|3|G2|C3|F3|A#3|D4|G4|
|4|G#2|C#3|F#3|**B3**|D#4|G#4|
|5|**A2**|**D3**|**G3**|C4|**E4**|A4|

__Your Task__

An empty ASCII tab should look like:

```
e |----------|
B |----------|
G |----------|
D |----------|
A |----------|
E |----------|
```

Given a string representing a sequence of notes, output an array of six strings with the correct numbers, where each element is a line of an ASCII tab as shown above. 

Ignore the rhythm (beats and rests) of the melody. There should be exactly one dash to the column on the left and on the right of each note. 

Include the string's note and a bar character, `|`, as shown, and end each line with a bar character.

For each note, write it on the lowest fret number possible (for example, if you have to write `B2`, write a `2` on the `A` string, not `7` on the `E` string.

__Examples__

The opening measure of Metallica's "Nothing Else Matters" is `E2 G3 B3 E4 B3 G3`

The beginning of "Joy to the World" is:

`D4 C#4 B3 A3`
`G3 F#3 E3 D3`
"""


description3 = """
You're learning the guitar and wish to practice playing simple melodies. You know the notes for the melodies, so you type them in a text file. Now all that's left is some code to output an [ASCII guitar tab](https://en.wikipedia.org/wiki/ASCII_tab)!

**Note**: If you have played guitar and are familiar with music theory, please skip to the section **Your Task**.

A note is a symbol from this repeating list (we are not using flats here):

`C, C#, D, D#, E, F, F#, G, G#, A, A#, B`
 
A note is followed by the octave it belongs to (roughly, how high-pitched it is). 

The octave number increases when moving from `B` to the following `C`.

Middle C on the piano is in the fourth octave, so its symbol is `C4`.

A guitar's *standard tuning* assigns the following pitches to the six strings, starting from the thickest one (the lowest pitched one):

`E2, A2, D3, G3, B3, E4`.

In the ASCII tab you will produce, the thinnest, `E4`, string appears first, on top. To tell the two `E` strings apart, `E2` is written as a capital `E` and `E4` as a lowercase `e`.

Placing a finger on a fret will produce a sharper note when picking that string. Each fret is one **semitone** higher than the previous one. Increasing a note by one semitone is equivalent to going one note to the right on the list of twelve notes above.

Note that all intervals between strings except between G3 and B3 are 5 semitones. From G3 to B3, there are 4 semitones.

A sound made by picking a string is represented by a number written on the corresponding line of the tab. A `0` means the string is *open*, that is, you don't touch any fret. A fretted note will be correspond to how many frets away it is from the top, starting with `1`.

![C chord](https://i.imgur.com/BFtGP3C.png)

(credit: Kiefer.Wolfowitz, Wikipedia)

In the diagram above, `G4` is being played. Placing a finger on the third fret is like increasing `E4` by three semitones: `E4 > F4 > F#4 > G4`. So, we write `3` on the `e` string:

```
e |-3-|
B |---|
G |---|
D |---|
A |---|
E |---|
```


As another example, 

```
e |---|
B |---|
G |---|
D |---|
A |-0-|
E |---|
```

means you should play the note `A2` without touching the fretboard. Observe that all other strings should have a dash,`-`, in the same column of the note played.

The complete note-to-fret table you will need is shown below. Note that the fifth fret will never be used; it is shown just to highlight how the same note can appear on different strings. However, on a real guitar, the quality of the note will sound different because of the string's physical differences.

(You may have to expand this side panel in order the see the entire table)

|Fret|E|A|D|G|B|e|
|--|--|--|--|--|--|--|
|0|E2|A2|D3|G3|B3|E4|
|1|F2|A#2|D#3|G#3|C4|F4|
|2|F#2|B2|E3|A3|C#4|F#4|
|3|G2|C3|F3|A#3|D4|G4|
|4|G#2|C#3|F#3|**B3**|D#4|G#4|
|5|**A2**|**D3**|**G3**|C4|**E4**|A4|

__Your Task__

An empty ASCII tab should look like:

```
e |----------|
B |----------|
G |----------|
D |----------|
A |----------|
E |----------|
```

Given a string representing a sequence of notes, output an array of six strings with the correct numbers, where each element is a line of an ASCII tab as shown above. 

Ignore the rhythm (beats and rests) of the melody. There should be exactly one dash to the column on the left and on the right of each note. 

Include the string's note and a bar character, `|`, as shown, and end each line with a bar character.

For each note, write it on the lowest fret number possible (for example, if you have to write `B2`, write a `2` on the `A` string, not `7` on the `E` string.

__Examples__

The opening measure of Metallica's "Nothing Else Matters" is `E2 G3 B3 E4 B3 G3`

The beginning of "Joy to the World" is:

`D4 C#4 B3 A3`
`G3 F#3 E3 D3`
"""

description2 = """
You're learning the guitar and wish to practice playing simple melodies. You know the notes for the melodies, so you write them in a string. Now all that's left is some code to output an [ASCII guitar tab](https://en.wikipedia.org/wiki/ASCII_tab)!

**Note**: If you have played guitar and are familiar with music theory, please skip to the section **Your Task**.

A note is a symbol from this repeating list (we are not using flats here):

`C, C#, D, D#, E, F, F#, G, G#, A, A#, B`
 
A note is followed by the octave it belongs to (roughly, how high-pitched it is). 

The octave number increases when moving from `B` to the following `C`.

Middle C on the piano is in the fourth octave, so its symbol is `C4`.

A guitar's *standard tuning* assigns the following pitches to the six strings, starting from the thickest one (the lowest pitched one):

`E2, A2, D3, G3, B3, E4`.

In the ASCII tab you will produce, the thinnest, `E4`, string appears first, on top. To tell the two `E` strings apart, `E2` is written as a capital `E` and `E4` as a lowercase `e`.

Placing a finger on a fret will produce a sharper note when picking that string. Each fret is one **semitone** higher than the previous one. Increasing a note by one semitone is equivalent to going one note to the right on the list of twelve notes above.

A sound made by picking a string is represented by a number written on the corresponding line of the tab. A `0` means the string is *open*, that is, you don't touch any fret. A fretted note will be correspond to how many frets away it is from the top, starting with `1`.

![C chord](https://i.imgur.com/BFtGP3C.png)

In the diagram above, `G4` is being played. Placing a finger on the third fret is like increasing `E4` by three semitones: `E4 > F4 > F#4 > G4`. So, we write `3` on the `e` string:

```
e |-3-|
B |---|
G |---|
D |---|
A |---|
E |---|
```


As another example, 

```
e |---|
B |---|
G |---|
D |---|
A |-0-|
E |---|
```

means you should play the note `A2` without touching the fretboard. Observe that all other strings should have a dash,`-`, in the same column of the note played.

The complete note-to-fret table you will need is shown below. Note that the fifth fret will never be used; it is shown just to highlight how the same note can appear on different strings. However, on a real guitar, the quality of the note will sound different because of the string's physical differences.

(You may have to expand this side panel in order the see the entire table)

|Fret|E|A|D|G|B|e|
|--|--|--|--|--|--|--|
|0|E2|A2|D3|G3|B3|E4|
|1|F2|A#2|D#3|G#3|C4|F4|
|2|F#2|B2|E3|A3|C#4|F#4|
|3|G2|C3|F3|A#3|D4|G4|
|4|G#2|C#3|F#3|**B3**|D#4|G#4|
|5|**A2**|**D3**|**G3**|C4|**E4**|A4|

__Your Task__

An empty ASCII tab should look like:

```
e |----------|
B |----------|
G |----------|
D |----------|
A |----------|
E |----------|
```

Given a string representing a sequence of notes, output an array of six strings with the correct numbers, where each element is a line of an ASCII tab as shown above. 

Ignore the rhythm (beats and rests) of the melody. There should be only one dash to the columns on the left and to the right of each note. 

Include the string's note and a bar character, `|`, as shown, and end each line with a bar character.

For each note, write it on the lowest fret number possible (for example, if you have to write `B2`, write a `2` on the `A` string, not `7` on the `E` string.

__Examples__

The opening measure of Metallica's "Nothing Else Matters" is `E2 G3 B3 E4 B3 G3`

The beginning of "Joy to the World" is:

`D4 C#4 B3 A3`
`G3 F#3 E3 D3`
"""

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


# simpleGuitarTab

The opening measure of Metallica's "Nothing Else Matters" is `E-2 G-3 B-3 E-4 B-3 G-3`

The beginning of "Joy to the World" is:

`D-4 C#4 B-3 A-3`
`G-3 F#3 E-3 D-3`



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



constraints = """
The melody, formatted as a space-separated sequence of notes (such as `C3` and `G#2`)


The equivalent 6-line guitar tab in standard tuning, where one line represents a string, with the thinnest string on top.
"""




range = ['E2',  # string E
         'F2',
         'F#2',
         'G2',
         'G#2',  
         'A2',  # string A
         'A#2',
         'B2',
         "C3",
         "C#3",
         "D3",  # string D
         "D#3",
         'E3',
         'F3',
         'F#3',
         'G3',  # string G
         'G#3',
         'A3',
         'A#3',
         'B3',  # string B
         "C4",
         "C#4",
         "D4",
         "D#4",
         'E4',  # string e
         'F4',
         'F#4',
         'G4',
         'G#4',
         'A4',
         'A#4',
         'B4',
         'C5',
         'C#5']

strings = [
    ['E4',  # string e
     'F4',
     'F#4',
     'G4',
     'G#4',
     'A4',
     'A#4',
     'B4',
     'C5',
     'C#5'],

    ['B3',  # string B
     "C4",
     "C#4",
     "D4",
     "D#4",],

    ['G3',  # string G
     'G#3',
     'A3',
     'A#3',],
        
    ["D3",  # string D
     "D#3",
     'E3',
     'F3',
     'F#3',],

    ['A2',  # string A
     'A#2',
     'B2',
     "C3",
     "C#3",],

    ['E2',  # string E
     'F2',
     'F#2',
     'G2',
     'G#2',],
]


fullFretTable = """
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
"""
