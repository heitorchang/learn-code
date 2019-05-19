"""
The much maligned `GOTO` statement had a significantly more insidious cousin named `GOSUB` (Go Subroutine).

In effect, a `GOSUB` and its partner-in-crime `RETURN` are like two `GOTO`s rolled into one. If this piqued your interest, read on. Otherwise, please maintain your sanity and click on the &larr; `Back` button on the top-left corner.

Still here? OK, good! 

In this hands-on computer history workshop, you may check your work with the [WebMSX](https://webmsx.org/) emulator (I grew up with one of these computers).

Like most BASICs of the time, a program consists of a list of strings, each of which started with a positive integer value (typically multiples of 10). The interpreter automatically sorted the lines you typed in.

Here's a very simple program:

```
10 A = 5
20 B = 3
30 PRINT A + B
```

When `RUN`, the interpreter will output

```
 8
Ok
```

Normally, the program will go in the order of the line numbers. For any non-trivial program though, the `GOTO X` and `GOSUB X` statements allow the programmer to control execution flow by making the program jump immediately to line `X`. 

The difference between `GOTO` and `GOSUB` is that `GOSUB` will save its own line number so that when a `RETURN` command is encountered, the program flow jumps back to this saved line number, and it proceeds with the next line in the program order. 

While a `GOTO` is done after it's executed, a `GOSUB` is active until a `RETURN` statement is reached and executed.

There may be a line number specified after `RETURN`. In this case, the program will jump to this line instead of the line where the active `GOSUB` command was called. This `GOSUB` is then completed after the jump.

XXXX When `GOSUB`s are nested, the interpreter has to keep track of

![manual](https://i.imgur.com/ZBuxxEo.png)

XXXX print "ERROR" if there's a return without gosub, missing returns, etc.

"""
