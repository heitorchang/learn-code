from itertools import islice

def generateSeries(start, multFactor):
    yield start

    while start >= 1:
        start *= multFactor
        yield start

def listFromGen(start, multFactor, howMany):
    return list(islice(generateSeries(start, multFactor), howMany))
