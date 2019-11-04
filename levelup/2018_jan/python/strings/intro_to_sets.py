"""
Task

Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used:

Input Format

The first line contains the integer, , the total number of plants.
The second line contains the  space separated heights of the plants.

Constraints


Output Format

Output the average height value on a single line.

Sample Input

10
161 182 161 154 176 170 167 171 170 174
Sample Output

169.375
Explanation

Here, set is the set containing the distinct heights. Using the sum() and len() functions, we can compute the average.
"""

def average(array):
    s = set(array)
    return sum(s) / len(s)


    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
