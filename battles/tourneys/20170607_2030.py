
def appleBoxes(k):
    b = []
    for i in range(1, k+1):
        b.append(i * i)
    odds = []
    evens = []
    for bb in b:
        if bb % 2 == 0:
            evens.append(bb)
        else:
            odds.append(bb)
    return sum(evens) - sum(odds)

def imageTruncation(image, threshold):
    
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] > threshold:            
                image[i][j] = threshold
    return image


def test():
    testeql(appleBoxes(5), -15)
    testeql(imageTruncation([[0, 100, 100], 
         [1, 255, 103]], 102), [[0,100,100], 
 [1,102,102]])
