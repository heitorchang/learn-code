def grabThatVine(vines):
    airplane = 99
    larry = 0
    uglyHack_maxTime = 1000
    
    grid = ["" for _ in range(airplane+1)]
    
    vObj = [{'left': 0, 'leftTimes': None, 'swingTime': 0}
            for _ in range(len(vines))]
    
    for i, v in enumerate(vines):
        vObj[i]['left'] = v[0]
        vObj[i]['leftTimes'] = list(range(0, uglyHack_maxTime, v[1] * 2))
        vObj[i]['swingTime'] = v[1]
        grid[v[0]+1:v[0]+4] = "qqq"
    
    onSolidGround = True
    quicksandPitNum = 0
    timer = 0
    
    while True:
        if larry == airplane:
            return timer

        print(timer, larry)
        if grid[larry+1] == 'q':
            if timer in vObj[quicksandPitNum]['leftTimes']:
                timer += vObj[quicksandPitNum]['swingTime']
                larry += 4
            else:
                for t in vObj[quicksandPitNum]['leftTimes']:
                    if t > timer:
                        timer = t
                        timer += vObj[quicksandPitNum]['swingTime']
                        larry += 4
                        break
            quicksandPitNum += 1
        else:
            larry += 1
            timer += 1
        
    return timer
