
def truncateString(s):

    def truncate(l, r):
        if l >= r:
            return ''
        newL = l
        newR = r
        left = ord(s[l]) - ord('0')
        right = ord(s[r - 1]) - ord('0')
        if left % 3 == 0:
            newL += 1
        elif right % 3 == 0:
            newR -= 1
        elif (left + right) % 3 == 0:
            newL += 1
            newR -= 1
        else:
            return s[l : (r)]

        return truncate(newL, newR)

    return truncate(0, len(s))


def arrayMaxConsecutiveSumTLE(inputArray, k):
    sums = []
    for i in range(len(inputArray)-k+1):
        sums.append(sum(inputArray[i:i+k]))
    return max(sums)
    # time limit exceeded

def arrayMaxConsecutiveSum(inputArray, k):
    maxSum = sum(inputArray[:k])
    newSum = maxSum
    for i in range(k, len(inputArray)):
        newSum = newSum + inputArray[i] - inputArray[i-k]
        if newSum > maxSum:
            maxSum = newSum
    return maxSum
    # time limit exceeded

def test():
    testeql(truncateString("312248"), "2")
    testeql(arrayMaxConsecutiveSum([2, 3, 5, 1, 6], 2), 8)
    testeql(arrayMaxConsecutiveSum([1,3,2,4], 3), 9)
