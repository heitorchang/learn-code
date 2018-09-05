def makeArrayConsecutive(sequence):
    s = sorted(sequence)
    r = []
    
    for i in range(len(s)-1):
        left = s[i]
        right = s[i+1]
        pr('left right')
        r.extend(range(left+1, right))
    return r
        

def lazyFriends(houses, maxDist):

    result = []
    left = 0
    right = 0
    for i in range(len(houses)):
        while houses[i] - houses[left] > maxDist:
            left -= 1
        while (right + 1 < len(houses)
                and houses[right + 1] - houses[i] > maxDist):
            right += 1
        result.append(right - left)

    return result


def test():
    testeql(makeArrayConsecutive([6, 2, 3, 8]), [4, 5, 7])
    testeql(lazyFriends([1, 2, 4, 8, 10],5), [2,2,3,2,1])
