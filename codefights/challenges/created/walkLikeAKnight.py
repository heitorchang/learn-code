draft_two = """

*Credit for this Challenge goes to @kov, I am just writing the description.*

As a noble knight of Chesslandia, you move along the squares on the board in an `L` shape. You've just become the **Prime Minister**, affording you **extra movement.**

With this change, you've lost the traditional ability to move two squares either horizontally or vertically, then one square perpendicularly.

Now, in one turn you may move `a` squares, then `b` squares such that `a` and `b` are two consecutive *prime numbers*, (2, 3, 5, 7, 11, 13, 17, etc.). 

There is no limit to how far you can move, as long as it's in an `L` shape and respecting the consecutive primes condition. For example, a move may be `(2, 3)`, `(7, 11)`, or `(127, 131)` squares.

Your office is located exactly at the center of an `n x n` board, where `n` is an odd number. On this board, you start at the coordinate location `(0, 0)`. Similar to a Cartesian grid, for a coordinate `(x, y)`, `+x` is to the right of, `-x` to the left of, `+y` above and `-y` below your starting point. 

`n` refers to the width and height of the board, so valid coordinates range from `-n / 2` to `n / 2` (rounded down).

You have to attend a ceremony in the *Top-Right Quarter* located at the given coordinates `(x, y)` (both non-negative). You may choose any valid move each turn. 

What is the minimum number of moves you must make to reach the destination?

"""


draft = """

*Credit for this Challenge goes to @kov, I am just writing the description.*

As a noble knight of Chesslandia, you move along the squares on the board in an `L` shape. You've just become the **Prime Minister**, affording you **extra movement.**

With this change, you've lost the traditional ability to move two squares either horizontally or vertically, then one square perpendicularly.

Now, in one turn you may move `a` squares, then `b` squares such that `a` and `b` are two consecutive *prime numbers*, (2, 3, 5, 7, 11, 13, 17, etc.). 

There is no limit to how far you can move, as long as it's in an `L` shape and respecting the consecutive primes condition. For example, a move may be `(2, 3)`, `(7, 11)`, or `(127, 131)` squares.

Your office is located exactly at the center of an `n x n` board, where `n` is an odd number. On this board, you start at the coordinate location `(0, 0)`. Similar to a Cartesian grid, for a coordinate `(x, y)`, `+x` is to the right of, `-x` to the left of, `+y` above and `-y` below your starting point. `n` refers to the width and height of the board, so valid coordinates range from `-n / 2` to `n / 2` (rounded down).

You have to attend a ceremony located at the given coordinates `(x, y)`. You may choose any valid move each turn. What is the minimum number of turns you must take to reach the destination?

"""


kov_js = """

// not exactly correct, because it returns 4 if all else fails
// but there are boards with expected values of 5 

primeKnight = (size, [Ay, Ax], [By, Bx]) => {
    console.log([Ay, Ax], [By, Bx])
    console.time()

    sieve = new Uint8Array(size)
    for (i = 2; i * i <= size; i++)
        if (sieve[i] == 0) 
            for (j = i + i; j <= size; j += i)
                sieve[j] = 1
    primes = []
    for (i = 3; i < size; i++)
        sieve[i] || primes.push(i)

    board = new Uint8Array(size * size)

    A = Ay * size + Ax
    B = By * size + Bx
    q = []
    r = []
    i = 2
    for (j of primes) {
        for ([Y, X] of [[Ay + i, Ax - j], [Ay + i, Ax + j], [Ay - i, Ax - j], [Ay - i, Ax + j], [Ay + j, Ax - i], [Ay + j, Ax + i], [Ay - j, Ax - i], [Ay - j, Ax + i]]) {
            C = Y * size + X
            if (C == B) {
                console.timeEnd()
                return 1
            }
            if (board[C] != 1)
                q.push([i, j])
            if (board[C] == 0) 
                board[C] = 1,
                r.push([Y, X])
            i = j
        }
    }
    console.log(primes.length, q.length, r.length)

    i = 2
    for ([i, j] of q) {
        C = (By + i) * size + Bx + j
        if (board[C] == 1) {
            console.timeEnd()
            return 2
        }
        if (board[C] == 0) {
            board[C] = 2
        }
    }
    for ([Ay, Ax] of r) {
        for ([i, j] of q) {
            C = (Ay + i) * size + Ax + j
            if (board[C] == 2) {
                console.timeEnd()
                return 3
            }
            if (board[C] == 0) 
                board[C] = 3
        }
    }
    console.timeEnd()
    return 4
}
console.log(primeKnight(size = 1e4, [Math.random() * size | 0, Math.random() * size | 0], [Math.random() * size | 0, Math.random() * size | 0]))

"""



gen = """

primeKnightBoard = (size) => {
    console.time()
    sieve = new Uint8Array(size + 1)
    for (i = 2; i * i <= size; i++)
        if (sieve[i] == 0) 
            for (j = i + i; j <= size; j += i)
                sieve[j] = 1
    primes = []
    for (i = 3; i < size; i++)
        sieve[i] || primes.push(i)

    size = size + 1 >> 1
    a = Array(size).fill(0).map(r => Array(size).fill(0))
    q = [[0, 0, 0]]
    a[0][0] = "x"
    for ([y, x, d] of q) {
        i = 2
        for (j of primes) {
            for ([Y, X] of [[i, j], [i, -j], [-i, j], [-i, -j], [j, i], [j, -i], [-j, i], [-j, -i]]) {
                Y += y
                if (Y < 0) Y = -Y
                X += x
                if (X < 0) X = -X
//                Y = Math.abs(Y + y)
//                X = Math.abs(X + x)
                if (Y < size && X < size && a[Y][X] === 0) 
                    a[Y][X] = d + 1,
                    q.push([Y, X, d + 1])
            }
            i = j
        }
    }
    a.map(r => console.log(r.join` `))
    console.timeEnd()
}

for (size = 7; size < 21; size += 2)
    console.log("---", size),
    primeKnightBoard(size)

"""


ans = """

primeKnightNoGood = (size, [Ay, Ax], [By, Bx]) => {
    console.log([Ay, Ax], [By, Bx])
    console.time()

    sieve = new Uint8Array(size)
    for (i = 2; i * i <= size; i++)
        if (sieve[i] == 0) 
            for (j = i + i; j <= size; j += i)
                sieve[j] = 1
    primes = []
    for (i = 3; i < size; i++)
        sieve[i] || primes.push(i)

    board = new Uint8Array(size * size)

    A = Ay * size + Ax
    B = By * size + Bx
    q = []
    r = []
    i = 2
    for (j of primes) {
        for ([Y, X] of [[Ay + i, Ax - j], [Ay + i, Ax + j], [Ay - i, Ax - j], [Ay - i, Ax + j], [Ay + j, Ax - i], [Ay + j, Ax + i], [Ay - j, Ax - i], [Ay - j, Ax + i]]) {
            C = Y * size + X
            if (C == B) {
                console.timeEnd()
                return 1
            }
            if (board[C] != 1)
                q.push([i, j])
            if (board[C] == 0) 
                board[C] = 1,
                r.push([Y, X])
            i = j
        }
    }
    console.log(primes.length, q.length, r.length)

    i = 2
    for ([i, j] of q) {
        C = (By + i) * size + Bx + j
        if (board[C] == 1) {
            console.timeEnd()
            return 2
        }
        if (board[C] == 0) {
            board[C] = 2
        }
    }
    for ([Ay, Ax] of r) {
        for ([i, j] of q) {
            C = (Ay + i) * size + Ax + j
            if (board[C] == 2) {
                console.timeEnd()
                return 3
            }
            if (board[C] == 0) 
                board[C] = 3
        }
    }
    console.timeEnd()
    return 4
}

primeKnight = (n, x, y) => {
  return primeKnightNoGood(size, [0, 0], [x, y])
}


"""

testCases = """

