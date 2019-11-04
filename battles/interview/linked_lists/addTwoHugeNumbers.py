# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):
    strA = ''
    strB = ''
    
    while True:
        strA += str(a.value).zfill(4)
        a = a.next
        if a is None:
            break
    
    while True:
        strB += str(b.value).zfill(4)
        b = b.next
        if b is None:
            break
    sumStr = str(int(strA) + int(strB))
    digits = len(sumStr)
    print(sumStr)
    firstChunkLen = digits % 4
    if firstChunkLen == 0:
        firstChunkLen = 4
    firstChunk = int(sumStr[:firstChunkLen])
    sumStr = sumStr[firstChunkLen:]
    ans = [firstChunk]
    for i in range(len(sumStr) // 4):
        ans.append(int(sumStr[i*4:i*4+4]))
                   
    return ans
