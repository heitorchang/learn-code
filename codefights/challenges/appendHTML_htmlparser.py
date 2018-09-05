from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self, target, toAdd):
        HTMLParser.__init__(self)
        self.myHTML = ""
        self.matchCt = 0
        self.matchTagType = []
        self.matchTagName = ""
        self.typ = "tagName"
        self.target = target
        if target[0] == ".":
            self.typ = "classes"
            self.target = self.target[1:]
        elif target[0] == "#":
            self.typ = "id"
            self.target = self.target[1:]
            
        self.toAdd = toAdd
        
    def handle_starttag(self, tag, attrs):
        if self.typ == "tagName" and tag == self.target:
            self.matchCt += 1
            self.matchTagType.append(tag)
        elif self.typ == "classes":
            # look for classes in attrs
            for t in attrs:
                if t[0] == 'class':
                    classes = t[1].split()
                    if self.target in classes:
                        self.matchCt += 1
                        self.matchTagType.append(tag)
                    break
        elif self.typ == "id":
            # look for id
            for t in attrs:
                if t[0] == 'id':
                    if self.target == t[1]:
                        self.matchCt += 1
                        self.matchTagType.append(tag)
                    break
                
        self.myHTML += self.get_starttag_text()

    def handle_data(self, data):
        self.myHTML += data

    def handle_startendtag(self, tag, attrs):
        self.myHTML += self.get_starttag_text()
        
    def handle_endtag(self, tag):
        if self.matchCt > 0 and tag == self.matchTagType[-1]:
            self.myHTML += self.toAdd
            self.matchCt -= 1
            self.matchTagType.pop()
        self.myHTML += "</" + tag + ">"
        

def appendHTML(htmlDoc, target, htmlString):
    parser = MyHTMLParser(target, htmlString)
    parser.feed(htmlDoc)
    return parser.myHTML
    
def test():
    # testeql(appendHTML("<div></div>", "div", "<p>9+ codefriends online</p>"), "<div><p>9+ codefriends online</p></div>")

    testeql(appendHTML("<div class=\"challenges codefight\"><h3>FAQ</h3></div><div class=\"codefight\"></div>", ".codefight", "<h4>Is it valid HTML5 to use a single tag for a div?</h4>"), "<div class=\"challenges codefight\"><h3>FAQ</h3><h4>Is it valid HTML5 to use a single tag for a div?</h4></div><div class=\"codefight\"><h4>Is it valid HTML5 to use a single tag for a div?</h4></div>")
    
    # testeql(appendHTML("<div><div></div><div><div></div><div><div></div><div></div></div></div></div>", "div", "<div>text</div>"), "<div><div><div>text</div></div><div><div><div>text</div></div><div><div><div>text</div></div><div><div>text</div></div><div>text</div></div><div>text</div></div><div>text</div></div>")

    testeql(appendHTML("<p data-hint=\"Anything can be here\"><img src=\"/sample.jpg\" alt=\"\" /></p>", "p", "<strong>Some content</strong>"), "<p data-hint=\"Anything can be here\"><img src=\"/sample.jpg\" alt=\"\" /><strong>Some content</strong></p>")
