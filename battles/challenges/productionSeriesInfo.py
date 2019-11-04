def productionSeriesInfo(ing, r1, r2, ser):
    arr = [0, r1, r2]
    consume = [0] * len(ser)
    for i in range(len(ser)):
        consume[i] = arr[ser[i]] if ser[i] <= 2 else ser[i]
    constot = sum(consume)
    canproduce = ing // constot
    if canproduce == 0:
        return ["Out of ingredients!", "Missing {} ingredients".format(constot - ing)]
    elif canproduce == 1:
        return ["Ok"]
    else:
        return ["Ok", "Ingredients for {} more series".format(canproduce - 1)]

test(productionSeriesInfo(16, 2, 5,[1, 1, 2, 1, 2]), ["Ok"],
     productionSeriesInfo(25, 1, 2, [1,1,3,2]), ["Ok", "Ingredients for 2 more series"])
