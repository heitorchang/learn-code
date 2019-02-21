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


kov_board = """

primeKnightBoard = (y, x) => {
    a = Array(y * 2).fill(0).map(r => Array(x * 2).fill(0))
    q = [[y, x, 0]]
    a[y][x] = false
    for ([y, x, d] of q) {
        i = 2
        for (j of [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997,  1009]) {

            [[y + i, x - j], [y + i, x + j], [y - i, x - j], [y - i, x + j], [y + j, x - i], [y + j, x + i], [y - j, x - i], [y - j, x + i]]
                .map(([Y, X]) => {
                    if ((a[Y] || 0)[X] === 0)
                        a[Y][X] = d + 1,
                        q.push([Y, X, d + 1])
                })
            i = j
        }
    }
    a.map(r => console.log(r.join``))
}
primeKnightBoard(1000, 1000)

"""
