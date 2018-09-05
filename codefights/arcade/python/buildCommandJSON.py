import json
from collections import OrderedDict

def clearDict(d):
    for k in d:
        if isinstance(d[k], str):
            d[k] = ''
        elif isinstance(d[k], int) or isinstance(d[k], float):
            d[k] = 0
        elif isinstance(d[k], list):
            d[k] = []
        elif isinstance(d[k], OrderedDict):
            d[k] = clearDict(d[k])
    return d

def buildCommand(jsonFile):
    po = json.JSONDecoder(object_pairs_hook=OrderedDict).decode(jsonFile)
    clearDict(po)
    return json.dumps(po)

def test():
    testeql(buildCommand("{\"version\": \"0.1.0\",\"command\": \"c:python\",\"args\": [\"app.py\"],\"problemMatcher\": {\"fileLocation\": [\"relative\", \"${workspaceRoot}\"],\"pattern\": {\"regexp\": \"^(.*)+s$\", \"message\": 1}}}"), "{\"version\": \"\", \"command\": \"\", \"args\": [], \"problemMatcher\": {\"fileLocation\": [], \"pattern\": {\"regexp\": \"\", \"message\": 0}}}")
