

def differentValues(a, d):
    maxDiff = -1
    for i in range(len(a)):
        for j in range(i, len(a)-1):
            ab = abs(a[i]-a[j])
            if ab <= d and ab > maxDiff:
                maxDiff = ab
    return maxDiff
    # did not pass


def test():
    testeql(
