description = """
Paranormal researchers have shown interest in your recording of ghosts' boos from the [*night at your aunt's haunted mansion*](https://app.codesignal.com/challenge/fBMqpka3pvk9jSHXp) (the **wailingGhosts** Challenge) and wish to further analyze its contents.

To recap, you recorded the noises you had heard as a string of low-pitched noises (represented as `o`) and high-pitched ones (represented as `u`). Each character is one decisecond (one-tenth of a second) long. Ghosts' boos follow a predictable pattern:

They begin with a non-zero length of `o`s, then a non-zero length of `u`s, followed by another length of `o`s that **is exactly the same length as the initial sequence of `o`s**. Other random noise was caused by the wind.

For example:

```
"ouo" = ghost (length 3)
"oouuuoo" = ghost (length 7)
"ouuooo" = ghost (len. 4) then wind (len. 2)
"uo" = wind (length 2)
```

Given an uninterrupted sequence of sounds, your task is to determine the maximal number of deciseconds out of the sequence that can be classified as ghost boos **(they do not overlap).**

__Examples__

For `sounds = "oouoo"`, you should output `5`. This is a typical ghost boo and it occupies the entire input. Though `ouo` is also a boo, we want the maximal length that can be counted as a boo.

For `sounds = "ouuooouo"`, you should output `7`. There are two ghost boos, `ouuo` and `ouo`. The `o` between them cannot be added to either side.

For `sounds = "uuuoooo"`, you should output `0`. Boos begin and end with at least one `o`.

For `sounds = "ouououo"`, you should output `6`. There is a `ouo` on both ends, and the middle `u` cannot be counted as a boo because boos do not overlap.

For `sounds = "ooouooouo"`, you should output `8`. The first `o` may be skipped to produce `oouoo` followed by `ouo`. There is another possibility, where we take the initial sequence `ooouooo`, but this is only `7` deciseconds long.

"""
