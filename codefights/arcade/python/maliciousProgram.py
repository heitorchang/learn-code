from datetime import datetime

def maliciousProgram(curDate, changes):
    d = datetime.strptime(curDate, "%d %b %Y %H:%M:%S")
    dArr = [d.day, d.month, d.year, d.hour, d.minute, d.second]
    m = [d + c for (d, c) in zip(dArr, changes)]

    try:
        modD = datetime(m[2], m[1], m[0], m[3], m[4], m[5])
        return modD.strftime("%d %b %Y %H:%M:%S")
    except ValueError:
        return curDate    
            
    print(modArr)

def test():
    testeql(maliciousProgram("28 Jan 1900 16:09:10", [1, 1, 0, 5, 10, 15]), "28 Jan 1900 16:09:10")
