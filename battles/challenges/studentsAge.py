from collections import defaultdict
def studentsAge(students):
    def hist(lst):
        res = defaultdict(int)
        for e in lst:
            res[e] += 1
        return res
    h = hist(students)
    len_s = len(students)
    tot = 0
    for i in range(1, len_s):
        h[students[i-1]] -= 1
        try:
            tot += h[students[i-1] + 1]
        except KeyError:
            pass
    return tot
