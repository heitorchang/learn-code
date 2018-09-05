def additionWithoutCarrying(a, b):
    stra = str(a)
    strb = str(b)

    # pad with zeros
    maxlen = max(len(stra), len(strb))
    stra = stra.zfill(maxlen)
    strb = strb.zfill(maxlen)
    ans = ""
    for da, db in zip(stra, strb):
        ans += str((int(da) + int(db)) % 10)
    return int(ans)

test(additionWithoutCarrying(456, 1734), 1180,
     additionWithoutCarrying(99999, 0), 99999,
     additionWithoutCarrying(999, 999), 888)
