description = """
Given an integer n, you can remove either its first or last digit in one step. After applying this operation several times, you'll get a number x with a length of k. It's possible that the number will contain leading zeros. What is the minimal and the maximal possible value of x that you can obtain?

Example

For n = 15243 and k = 2, the output should be
removeDigits(n, k) = [15, 52].

To obtain the minimal number with a length of k, we can use the following sequence of operations: 15243 -> 1524 -> 152 -> 15;
To obtain the maximal number with a length of k, we can use the following sequence of operations: 15243 -> 1524 -> 152 -> 52.
For n = 123 and k = 1, the output should be
removeDigits(n, k) = [1, 3].
"""

def removeDigits(n, k):
    """Instead of simulating step-by-step removal of digits (which would create a tree), realize that the final integer must be a contiguous sequence of digits."""
    
    s = str(n)
    substrs = []
    for start in range(len(str(n))-k+1):
        substrs.append(s[start:start+k])
    ints = [int(n) for n in substrs]
    return [min(ints), max(ints)]
