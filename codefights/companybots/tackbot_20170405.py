def requestMatching(pros, distances, travelPreferences):
    m = []

    for i in range(len(distances)):
        if distances[i] <= travelPreferences[i]:
            ms = distances[i]
        else:
            ms = distances[i] - travelPreferences[i]
        m.append(ms)
    print(list(reversed(sorted(zip(m, pros))))[:5])

def test():
    testeql(requestMatching(["Michael", 
 "Mary", 
 "Ann", 
 "Nick", 
 "Dan", 
 "Mark"],
[12, 10, 19, 15, 5, 20],[12, 8, 25, 10, 3, 10]), ["Michael", 
 "Ann", 
 "Dan", 
 "Mary", 
 "Nick"])
