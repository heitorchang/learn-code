finaldraft = """


https://app.codesignal.com/challenge/HZmffpDcxnWtZb9Bh


Mrs. DeNero's kitchen faucet isn't working anymore, and she hired a plumber, Ligia, to take a look. 

However, the kitchen wall is covered with precious antique tiles and Mrs. DeNero hopes Ligia breaks as few of them as possible. Behind each tile is a portion (a rectangular unit) of the plumbing that Ligia can replace.

Ligia has a special magnetic sensor that will indicate the pipes' shapes behind each tile, and what she found was appalling. It looks like gremlins scrambled everything!

Ligia asked you to help her optimize the repair job by finding the **minimum amount of tiles needed to be broken** to access the pipes behind them and make water flow again.

There are eleven types of pipes Ligia can use, and she has &infin; of each at her disposal. They are represented by these Unicode "box-drawing characters":

```
U+2550 ═
U+2551 ║
U+2554 ╔
U+2557 ╗
U+255A ╚
U+255D ╝
U+2560 ╠
U+2563 ╣
U+2566 ╦
U+2569 ╩
U+256C ╬
```

The source of the water is located at the top-left corner, and the faucet is located at the bottom-right corner. In both locations, water must flow horizontally from left to right.

In other words, the acceptable types of pipe to be used on the top-left corner must have an opening toward the left side, and the pipe used on the bottom-right corner (the faucet) must have an opening toward the right.

Whenever a pipe is not connected to another pipe, the water flow will stop there. Mrs. DeNero isn't so concerned about wasting water; she only wants to preserve her antique tiles. It's OK to use pipes that lead nowhere because Ligia can seal them.

__Examples__

In this scenario (Test 1),

![pipes 1](https://i.imgur.com/80r4prG.png)

only one tile needs to be broken: the one to the left of the faucet. It may be replaced with ═ , ╚ , ╩ , ╦ , ╠ or ╬. You should output `1`.

In Test 2, the pipes are already in the right place. Ligia says they were just clogged. The output should be `0`.

![pipes 2](https://i.imgur.com/rTkcfPJ.png)

"""

description = """

Mrs. DeNero's kitchen faucet isn't working anymore, and she hired a plumber, Ligia, to take a look. 

However, the kitchen wall is covered with precious antique tiles and Mrs. DeNero hopes Ligia breaks as few of them as possible.

Ligia has a special magnetic sensor that will indicate the pipes' shapes behind each tile, and what she found was appalling. It looks like gremlins scrambled everything!

Ligia asked you to help her optimize her repair job by finding the **minimum amount of tiles needed to be broken** to access the pipes behind them and make water flow again.

There are eleven types of pipes Ligia can use, and she has &infin; of each at her disposal. They are represented by these Unicode "box-drawing characters":

```
U+2550 ═
U+2551 ║
U+2554 ╔
U+2557 ╗
U+255A ╚
U+255D ╝
U+2560 ╠
U+2563 ╣
U+2566 ╦
U+2569 ╩
U+256C ╬
```

The source of the water is located at the top-left corner, and the faucet is located at the bottom-right corner. In both locations, water must flow horizontally from left to right.

In other words, the acceptable types of pipe to be used on the top-left corner must have an opening toward the left side, and the pipe used on the bottom-right corner (the faucet) must have an opening toward the right.

Whenever a pipe is not connected to another pipe, the water flow will stop there. Mrs. DeNero isn't so concerned about wasting water; she only wants to preserve her antique tiles.



"""


kov_draw_path = """

spaghettiPlumbing = P => {
    /* char map:
     * 9552 9553 9556 9559 9562 9565 9568 9571 9574 9577 9580 
     *  --   |    ,-   -,   '-   -'   |-   -|  -,-  -'-   + 
     * 1100 0011 0101 1001 0110 1010 0111 1011 1101 1110 1111   
     * lrud
     */
    console.time()
    h = P.length
    w = P[0].length
    M = P.map(r => 
        [...r].map(v => 
            [12, 3, 5, 9, 6, 10, 7, 11, 13, 14, 15][(v.charCodeAt(0) - 9550) / 3 | 0]
        )
    )
    M[0][-1] = M[h - 1][w] = 12
    q = [[[0, -1, 0, 8, []]]]
    m = 1 / 0
    V = []
    mod = {
        1: [, '\u2502', '\u250c', '\u2510'],
        2: ['\u2502', , '\u2514', '\u2518'],
        4: ['\u250c', '\u2514', , '\u2500'],
        8: ['\u2510', '\u2518', '\u2500', ]
    }
    for (r of q) 
        if (r) {
            for ([y, x, d, j, s] of r) 
                if (y in M && x in M[y]) {
                    v = M[y][x]
                    c = (v & j) < 1
                    if (y == h - 1 && x == w && m > d + c) {
                        m = d + c
                        path = s
                    }
                    if (V[y * w + x] <= d + c) continue
                    V[y * w + x] = d + c
                    for (i = 0; i < 4; i++) 
                        if (2 ** i - j) {
                            e = c | (v & 2 ** i) < 1
                            q[e += d] || (q[e] = [])
                            q[e].push(
                                [y + [1, -1, 0, 0][i], 
                                 x + [0, 0, 1, -1][i], 
                                 e, [2, 1, 8, 4][i], 
                                 [...s, [y,x,mod[j][i]]],
                                 //console.log(j,i, mod[j][i])
                                ])
                        }
                }
            if (m < 1 / 0)
                break
        }
    P.map(r => console.log(r))
    console.log("")

    P = P.map(r => [...r])
    for ([y, x, p] of path)
        P[y][x] = p
    P.map(r => console.log(r.join``))
        
    console.timeEnd()
    return m
}
/* 
function spaghettiPlumbing(pipes) {
    // char map:
    // 9552 9553 9556 9559 9562 9565 9568 9571 9574 9577 9580 
    //  --   |    ,-   -,   '-   -'   |-   -|  -,-  -'-   + 
    // 1100 0011 0101 1001 0110 1010 0111 1011 1101 1110 1111   
    // lrud

    console.time()
    h = pipes.length
    w = pipes[0].length
    map = pipes.map(r => 
        [...r].map(v => 
            [12, 3, 5, 9, 6, 10, 7, 11, 13, 14, 15][(v.charCodeAt(0) - 9550) / 3 | 0]
        )
    )
    map[0][-1] = map[h - 1][w] = 12
    q = [[[0, -1, 0, 15, 0]]]
    m = 1 / 0
    vis = []
    u = z = 0
    for (row of q) {
        if (row) {
            for ([y, x, d, j] of row) {
                u++
                if (y in map && x in map[y]) {
                    v = map[y][x]
                    c = (v & j) < 1
                    if (y == h - 1 && x == w) {
                        if (m > d + c) {
                            m = d + c
                        }
                    }
                    if (vis[y * w + x] <= d + c) continue
                    z++
                    vis[y * w + x] = d + c
                    for (i = 0; i < 4; i++) {
                        if (2 ** i - j) {
                            e = c | (v & 2 ** i) < 1
                            if (!q[d + e]) q[d + e] = []
                            q[d + e].push([y + [1, -1, 0, 0][i], x + [0, 0, 1, -1][i], d + e, [2, 1, 8, 4][i]])
                        }
                    }
                }
            }
        }
        if (m < 1 / 0)
            break
    }
    console.log(u, z, m)
    console.timeEnd()

    return m
}


/* board generator:
max = 400
pipes = Array(max)
    .fill()
    .map(r => 
         Array(max)
         .fill()
         .map(c => 
              String.fromCharCode([9552,9553,9556,9559,9562,9565,9568,9571,9574,9577,9580][Math.random() * 11 | 0])
          ).join``
     )
console.log(JSON.stringify(pipes).split`,`.join`,\n`)
spaghettiPlumbing(pipes)
*/

"""
