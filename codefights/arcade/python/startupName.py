def startupName(companies):
    comp1 = set(companies[0])
    comp2 = set(companies[1])
    comp3 = set(companies[2])
    all3 = (comp1 & comp2 & comp3)
    only1 = comp1 - (comp2 | comp3)
    only2 = comp2 - (comp1 | comp3)
    only3 = comp3 - (comp2 | comp1)

    pr('only1 only2 only3')
    onlyOne = only1 | only2 | only3

    allTotal = comp1 | comp2 | comp3
    answer = allTotal - onlyOne - all3

    pr('answer')
    res = (comp1 | comp2 | comp3) - ((comp1 - (comp2 | comp3)) | (comp2 - (comp1 | comp3)) | (comp3 - (comp2 | comp1))) - (comp1 & comp2 & comp3)
    
    return list(sorted(list(res)))

def test():
    testeql(startupName(["coolcompany", 
                         "nicecompany",
                         "legendarycompany"]), ["e", "l"])
