def drawRectangle(canvas, rectangle):
    for i in range(rectangle[0] + 1, rectangle[2]):
        canvas[rectangle[1]][i] = '-'
        canvas[rectangle[3]][i] = '-'
    for i in range(rectangle[1] + 1, rectangle[3]):
        canvas[i][rectangle[0]] = '|'
        canvas[i][rectangle[2]] = '|'
    for i in range(0, 4, 2):
        for j in range(1, 4, 2): # bugfix this line
            canvas[rectangle[j]][rectangle[i]] = '*'
    return canvas
    
def test():
    testeql(drawRectangle([["a","a","a","a","a","a","a","a"], 
 ["a","a","a","a","a","a","a","a"], 
 ["a","a","a","a","a","a","a","a"], 
 ["b","b","b","b","b","b","b","b"], 
 ["b","b","b","b","b","b","b","b"]], [1,1,4,3]), None)
