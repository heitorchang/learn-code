import re
from collections import namedtuple

import operator

def questionCorrectionBot(question):
    output = question.strip()
    output = output[0].upper() + output[1:]
    output = output.replace("?", "")
    output += "?"
    whitespaces = re.compile(r'\s+')
    output = whitespaces.sub(' ', output)

    commaPat = re.compile(r'\s*,\s*')
    output = commaPat.sub(', ', output)
    return output

def typeaheadSearch(queries):
    Row = namedtuple('Row', 'order, type, id, score, data')
    db = []
    order = 0
    result = []
    for q in queries:
        cmd = q[0]
        if cmd == "ADD":
            db.append(Row(order, q[1], q[2], float(q[3]), q[4].lower()))
            order += 1
        elif cmd == "DEL":
            r = 0
            for row in db:
                if row.id == q[1]:
                    del db[r]
                    break
                r += 1
        elif cmd == "QUERY":
            queryResult = []
            limit = int(q[1])
            searchTokens = q[2].lower().split()
            preliminaryMatches = []
            r = 0
            for row in db:
                match = True
                for t in searchTokens:
                    if row.data.find(t) == -1:
                        match = False
                        break
                if match:
                    # print(searchTokens, "matched", row)
                    preliminaryMatches.append(row)
                preliminaryMatches = sorted(preliminaryMatches, key=operator.attrgetter('score', 'order'), reverse=True)
            for p in preliminaryMatches:
                queryResult.append(p.id)
            result.append(queryResult[:limit])
    return result

def ontology(treeRepr, questions, queries):
    Node = namedtuple('Node', 'name, children, parent')
    treeReprParts = treeRepr.split()

    tree = Node(treeReprParts[0], [], None)

    curNode = tree
    for p in treeReprParts[1:]:
        if p == "(":
            curParent = curNode
        elif p == ")":
            curParent = curNode.parent
        else:
            newNode = Node(p, [], curParent)
            curParent.children.append(newNode)
            curNode = newNode
    pr('tree')
    # Give up
    
def test():
    testeql(ontology("Animals ( Reptiles Birds ( Eagles Pigeons Crows ) )", [
        "Reptiles: Why are many reptiles green?",
        "Birds: How do birds fly?",
        "Eagles: How endangered are eagles?",
        "Pigeons: Where in the world are pigeons most densely populated?",
        "Eagles: Where do most eagles live?"
    ],
                     ["Eagles How en",
                      "Birds Where",
                      "Reptiles Why do",
                      "Animals Wh"]), [1,2,0,3])
