def addBorder(picture):
    rows = len(picture)
    cols = len(picture[0])

    topBottom = '*' * (cols + 2)
    result = [topBottom]

    for r in range(rows):
        result.append('*' + picture[r] + '*')

    result.append(topBottom)
    return result
