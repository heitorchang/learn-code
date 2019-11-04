**WARNING:** Very long challenge description ahead and GO[TO/SUB] statements considered harmful by academics. Implementing GOSUB, however, may enrich your programming knowledge.

If you're familiar with `GOSUB`, `GOTO` the section **Your Task**.

Calling `GOSUB X` makes the program jump to the line numbered `X`, and when a `RETURN` statement is encountered, the program jumps back to where the `GOSUB` was called, proceeding with the next line.

`GOSUB`s may be nested (while there is available memory), and a `RETURN` will take the program back to the most recent `GOSUB`.

In this hands-on computer history workshop, we will work with the `MSX-BASIC` variety of BASIC because there is the top-notch [WebMSX emulator](https://webmsx.org/) that you may use to check your work.

In the emulator, you type a BASIC program directly, line-by-line. 

After typing a program, `F5` runs it, `F9` pauses it, and `Ctrl + F9` stops it. The `list` command prints the entire program you have typed so far, and `new` erases your program.

Like most BASICs of the time, a program consists of a list of strings, each of which starts with a positive integer value (typically multiples of 10, but any integer is valid). The interpreter automatically sorts the lines you typed in.

Consider this program:

```
10 PRINT "AN AUSPICIOUS BEGINNING"
20 GOSUB 100
30 PRINT "AFTER GOING TO SUB"
40 END
100 PRINT "SUBROUTINE IN LINE ONE-HUNDRED"
110 RETURN
```

When `RUN`, the output is:

```
AN AUSPICIOUS BEGINNING
SUBROUTINE IN LINE ONE-HUNDRED
AFTER GOING TO SUB
```

After `PRINT`ing the string in line `10`, the `GOSUB` takes us to line `100`, which `PRINT`s `SUBROUTINE ...`.

`RETURN` takes us back to the line immediately after `20`, the source of the `GOSUB`. This will be line `30`, which `PRINT`s `AFTER GOING TO SUB`. 

Finally, `END` signals the interpreter to stop. 

The statements you will encounter in this challenge are:

* `X = [expression]` This is an *assignment* expression that puts the value of *expression* in the variable `X`. 

For example, `X = 31`. Variables are global. They are named as a single uppercase character and only hold integers in this challenge.

Arithmetic operators used in assignments are `+`, `-` and `*`.

* `PRINT [expression]` The expression will be a string (enclosed in double quotes) or a variable. Double quotes will appear as `\"` in the given input because of the challenges platform restriction; the backslash should be ignored if you choose to use the WebMSX emulator.

* `GOSUB [line number]` Will make the program jump to *line number*.
 
* `RETURN` Will take the program back to the most recent `GOSUB`.

Let's investigate a handbook's sample and add some debugging `PRINT`s:

![diagram scan](https://i.imgur.com/ZBuxxEo.png)

```
1 PRINT "BEGIN MAIN"
10 GOSUB 100
20 PRINT "AFTER 100"
30 PRINT "END OF MAIN"
40 END

100 PRINT "SUB 100"
110 GOSUB 1000
190 PRINT "END OF SUB 100"
200 RETURN

1000 PRINT "SUB 1.000"
1900 PRINT "END OF SUB 1.000"
2000 RETURN
```

The output will be:

```
BEGIN MAIN
SUB 100
SUB 1.000
END OF SUB 1.000
END OF SUB 100
AFTER 100
END OF MAIN
```

__Your Task__

Given a BASIC program as an array of strings, where each string is a line of code, **output the first ten (or fewer) lines** of `PRINT` output generated by the given program. The output should be an array of strings, one for each line.

Even if `PRINT` output are numbers, your output should convert them to strings. Remove trailing and leading whitespace too.

The program will either end without errors or run into an infinite loop that prints at least ten lines. You do not need to check for errors. 

In case an infinite loop is created, the code may not necessarily have a `RETURN` statement for every `GOSUB`.

After the last statement is executed, the program stops, provided there is no infinite loop.