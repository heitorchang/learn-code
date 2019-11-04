description = """
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false;

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

1 3  2 3
 2 -1 1
1 2 3 2
1 5 2 3
1 5 4 3
"""

def isStrictlyIncreasing(a):
    for i in range(len(a)-1):
        if a[i+1] - a[i] <= 0:
            return False
    return True

def almostIncreasingSequence(sequence):
    for i in range(len(sequence)-1):
        if sequence[i+1] - sequence[i] <= 0:
            # Remove either the left or right number creating the nonincreasing sequence
            print(sequence[i], sequence[i+1])
            print(sequence[:i] + sequence[i+1:])
            print(sequence[:i+1] + sequence[i+2:])
            return isStrictlyIncreasing(sequence[:i] + sequence[i+1:]) or isStrictlyIncreasing(sequence[:i+1] + sequence[i+2:])
    return True

def test():
    testeql(almostIncreasingSequence([1, 3, 2, 1]), False)
    testeql(almostIncreasingSequence([1, 3, 2]), True)
    testeql(almostIncreasingSequence([1, 2, 1, 2]), False)
    testeql(almostIncreasingSequence([10, 1, 2, 3, 4, 5]), True)
    testeql(almostIncreasingSequence([1, 2, 3]), True)
    testeql(almostIncreasingSequence([1, 2, 3, 4, 3, 6]), True)
    
