from collections import Counter

def number_needed(a, b):
    ca = Counter(a)
    cb = Counter(b)
    da = ca-cb
    db = cb-ca
    return sum(da.values()) + sum(db.values())

a = input().strip()
b = input().strip()

print(number_needed(a, b))
