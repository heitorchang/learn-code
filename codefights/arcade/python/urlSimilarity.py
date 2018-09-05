from urllib.parse import urlparse

def samePaths(p1, p2):
    numSame = 0
    for i in range(min(len(p2), len(p1))):
        if p1[i] == p2[i]:
            numSame += 1
        else:
            break
    return numSame

def queryStrToDict(qs):
    if qs == [""]:
        return {}
    else:
        result = {}
        for s in qs:
            try:
                vals = s.split("=")
                result[vals[0]] = vals[1]
            except IndexError:
                pass
            except ValueError:
                pass
        return result
    
def urlSimilarity(url1, url2):
    p1 = urlparse(url1)
    p2 = urlparse(url2)

    similarity = 0
    if p1.scheme == p2.scheme:
        similarity += 5
    if p1.netloc == p2.netloc:
        similarity += 10

    path1 = p1.path.split("/")[1:]
    path2 = p2.path.split("/")[1:]
    similarity += samePaths(path1, path2)

    queries1 = queryStrToDict(p1.query.split("&"))
    queries2 = queryStrToDict(p2.query.split("&"))

    params1 = set(queries1.keys())
    params2 = set(queries2.keys())

    sharedParams = params1 & params2
    if sharedParams:    
        similarity += len(sharedParams)
        for p in sharedParams:
            if queries1[p] == queries2[p]:
                similarity += 1
    return similarity

def test():
    # testeql(urlSimilarity("https://codefights.com/home/test?param1=42&param3=testing&login=admin", "https://codefights.com/home/secret/test?param3=fish&param1=42&password=admin"), 19)

    # testeql(urlSimilarity("https://www.google.com/search?q=codefights", "http://www.google.com/search?q=codefights"), 13)

    testeql(urlSimilarity("ftp://www", "http://anotherexample.com/www?ftp=http"), 0)

    testeql(urlSimilarity("ftp://www.example.com", "http://example.com/query?varName=value"), 0)
