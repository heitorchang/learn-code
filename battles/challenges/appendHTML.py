import re
from collections import namedtuple

Tag = namedtuple("Tag", "name id classes children")

def parseHTML(s):
    pr('s')
    openPat = re.compile(r'<([^/]*?)>')
    openTagMatch = openPat.search(s)
    if openTagMatch:
        openTagParts = openTagMatch.groups()[0].split()
        tag = Tag(openTagParts[0], "", "", [])

        openTagL = openTagMatch.span()[0]
        openTagR = openTagMatch.span()[1]
        tag.children.append(parseHTML(s[:openTagL]))
        tag.children.append(parseHTML(s[openTagR:]))
        return tag
    return s
    
def appendHTML(htmlDoc, target, htmlString):
    p = parseHTML("<WRAP>abc<p>para</p></WRAP>")
    pr('p')

    # p2 = parseHTML("abc<p>para<b>bold</b>cde</p>")
    # pr('p2')
    
    # n = parseHTML("<p>abc<b>bold</b>def</p>")
    # pr('n')
    # n2 = parseHTML("<p>abc<b>bold</b>def<i>ital</i>ghi</p>")
    # pr('n2')
    # parseHTML(htmlDoc)

def test():
    # testeql(appendHTML("<div></div>", "div", "<p>9+ codefriends online</p>"), "<div><p>9+ codefriends online</p></div>")
    
    # testeql(appendHTML("<div class=\"challenges codefight\"><h3>FAQ</h3></div><div class=\"codefight\"></div>", ".codefight", "<h4>Is it valid HTML5 to use a single tag for a div?</h4>"), "<div class=\"challenges codefight\"><h3>FAQ</h3><h4>Is it valid HTML5 to use a single tag for a div?</h4></div><div class=\"codefight\"><h4>Is it valid HTML5 to use a single tag for a div?</h4></div>")
    
    # testeql(appendHTML("<div><div></div><div><div></div><div><div></div><div></div></div></div></div>", "div", "<div>text</div>"), "<div><div><div>text</div></div><div><div><div>text</div></div><div><div><div>text</div></div><div><div>text</div></div><div>text</div></div><div>text</div></div><div>text</div></div>")

    testeql(appendHTML("<p></p>", "p", "abc"), "<p>abc</p>")
