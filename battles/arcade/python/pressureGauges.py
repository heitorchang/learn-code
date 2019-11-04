def pressureGauges(morning, evening):
    combined = list(zip(morning, evening))
    pr('combined')
    report = [list(map(min, combined)), list(map(max, combined))]
    return [list(map(min, list(zip(morning, evening)))), list(map(max, list(zip(morning, evening))))]

def test():
    testeql(pressureGauges([3, 5, 2, 6], [1,6,6,6]), [[1,5,2,6],[3,6,6,6]])
