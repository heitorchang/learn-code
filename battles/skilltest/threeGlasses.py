def threeGlasses(cap):
    cap = sorted(cap)
    water = cap[:]
    amounts = set()
    amounts.add(cap[0])
    amounts.add(cap[1])
    amounts.add(cap[2])
    amounts.add(cap[0] + cap[1])
    amounts.add(cap[0] + cap[2])
    amounts.add(cap[1] + cap[2])
    amounts.add(sum(cap))
    
    def record():
        # add up current amount
        amounts.add(sum(water))
        
    def action(water):
        print(water)
        record()
        if water[0] > 0 and water[1] > 0 and water[2] > 0:
            action([0, water[1], water[2]])
        elif water[0] == 0 and water[1] > 0 and water[2] > 0:
            # pour from middle
            
            action([cap[0], max(0, water[1] - cap[0]), water[2]])
            action([cap[0], water[1], water[2] - cap[0]])
        elif water[0] == 0 and water[1] == 0 and water[2] > 0:
            action([0, cap[1], water[2] - cap[1]])
            action([cap[0], water[1], water[2] - cap[0]])

    while sum(water) > 0:
        action(water)

def test():
    testeql(threeGlasses([16,5,3]), 21)
