from html.parser import HTMLParser

class P(HTMLParser):
    def __init__(self, t, A):
        HTMLParser.__init__(self)
        self.H = ""
        self.C = 0
        self.T = []
        self.y = "N"
        self.t = t
        if t[0] == ".":
            self.y = "c"
            self.t = self.t[1:]
        elif t[0] == "#":
            self.y = "id"
            self.t = self.t[1:]
            
        self.A = A
        
    def handle_starttag(self, g, at):
        if self.y == "N" and g == self.t:
            self.C += 1
            self.T.append(g)
        elif self.y == "c":
            # look for c in at
            for t in at:
                if t[0] == 'class':
                    c = t[1].split()
                    if self.t in c:
                        self.C += 1
                        self.T.append(g)
                    break
        elif self.y == "id":
            # look for id
            for t in at:
                if t[0] == 'id':
                    if self.t == t[1]:
                        self.C += 1
                        self.T.append(g)
                    break
                
        self.H += self.get_starttag_text()

    def handle_data(self, data):
        self.H += data

    def handle_startendtag(self, g, at):
        self.H += self.get_starttag_text()
        
    def handle_endtag(self, g):
        if self.C > 0 and g == self.T[-1]:
            self.H += self.A
            self.C -= 1
            self.T.pop()
        self.H += "</" + g + ">"
        

def appendHTML(h, t, S):
    parser = P(t, S)
    parser.feed(h)
    return parser.H
    
def test():
    # testeql(appendHTML("<div></div>", "div", "<p>9+ codefriends online</p>"), "<div><p>9+ codefriends online</p></div>")

    testeql(appendHTML("<div class=\"challenges codefight\"><h3>FAQ</h3></div><div class=\"codefight\"></div>", ".codefight", "<h4>Is it valid HTML5 to use a single tag for a div?</h4>"), "<div class=\"challenges codefight\"><h3>FAQ</h3><h4>Is it valid HTML5 to use a single tag for a div?</h4></div><div class=\"codefight\"><h4>Is it valid HTML5 to use a single tag for a div?</h4></div>")
    
    # testeql(appendHTML("<div><div></div><div><div></div><div><div></div><div></div></div></div></div>", "div", "<div>text</div>"), "<div><div><div>text</div></div><div><div><div>text</div></div><div><div><div>text</div></div><div><div>text</div></div><div>text</div></div><div>text</div></div><div>text</div></div>")

    testeql(appendHTML("<p data-hint=\"Anything can be here\"><img src=\"/sample.jpg\" alt=\"\" /></p>", "p", "<strong>Some content</strong>"), "<p data-hint=\"Anything can be here\"><img src=\"/sample.jpg\" alt=\"\" /><strong>Some content</strong></p>")
