from collections import defaultdict
import xml.etree.ElementTree as ET

def printAllChildren(node, level, seen, tagOrder, tagKeys):
    tag = node.tag
    keys = node.keys()
    for k in keys:
        tagKeys[tag].add(k)
    if tag not in seen:
        seen.add(tag)
        tagOrder.append((tag, level))
    if node:
        for child in node:
            printAllChildren(child, level+1, seen, tagOrder, tagKeys)
    return tagOrder, tagKeys

def xmlTags(xml):
    root = ET.fromstring(xml)
    tagOrder, tagKeys = printAllChildren(root, 0, set(), [], defaultdict(set))
    result = []
    for tag in tagOrder:
        result.append("--" * tag[1] + tag[0] + "(" + ", ".join(sorted(tagKeys[tag[0]])) + ")")
    return result
    
def test():
    testeql(xmlTags("<data><animal name=\"cat\"><genus>Felis</genus><family name=\"Felidae\" subfamily=\"Felinae\"/><similar name=\"tiger\" size=\"bigger\"/></animal><animal name=\"dog\"><family name=\"Canidae\" member=\"canid\"/><order>Carnivora</order><similar name=\"fox\" size=\"similar\"/></animal></data>"),
            ["data()", 
             "--animal(name)", 
             "----genus()", 
             "----family(member, name, subfamily)", 
             "----similar(name, size)", 
             "----order()"])
