The hack is to return a formatted string. I created a custom task to test this, though the behavior is odd. If the expected answers in different tests are of different precisions, you might not pass all tests.

```
myround <- function(x, digits) {
    return(format(round(x, digits), nsmall=digits))
}
```

My task was to return the reciprocal of an integer. I created 3 tests, one for 2 (expecting 0.5), and two tests with 6 (expecting 0.1666...). One test expected 0.167 and the other, 0.1666666667. The 0.167 test would only pass if digits = 3, while the other test only passed with digits >= 5. However, with this larger precision, the 0.167 test would fail! That's what I mean that the behavior is odd. It shouldn't even accept a string, in my opinion, because the expected answer is a float

```
myReciprocal <- function(arg1) {
    return(myround(1 / arg1, 3))
}
```