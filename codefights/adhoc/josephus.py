def josephusProblem(n, k):
    """
Imagine the following situation for a given integers n and k. There are n people standing in a circle. They are numbered from 1 through n in clockwise direction. The counting out begins at person #1 and continues around the circle in a clockwise direction. In each step, k-1 people are skipped and the next person is removed from the circle. The elimination proceeds around the circle (which is becoming smaller and smaller as people get removed), until only one person remains, who is announced a winner.

The task is to find the place in the initial circle that would guarantee a win.

Example

For n = 3 and k = 2, the output should be
josephusProblem(n, k) = 3.
    """

    places = list(range(1, n+1))
    pointer = 0
    while len(places) > 1:
        pointer = (pointer + k-1) % len(places)
        places.pop(pointer)
        print(pointer, places)
    return places[0]
    
def test():
    testeql(josephusProblem(3, 2), 3)
