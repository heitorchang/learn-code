from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.depth = 0
        self.maxDepth = 0
        self.tags = set()

    def handle_starttag(self, tag, attrs):
        self.depth += 1
        if self.depth > self.maxDepth:
            self.maxDepth += 1
            self.tags = set([tag])
        elif self.depth == self.maxDepth:
            self.tags.add(tag)

    def handle_endtag(self, tag):
        self.depth -= 1
        
    def getTags(self):
        return self.tags
    
def pageComplexity(document):
    parser = MyHTMLParser()
    parser.feed(document)
    return sorted(parser.getTags())

def test():
    testeql(pageComplexity("<!DOCTYPE html><html>  <body>    <h1>The best heading ever</h1>    <!--Actually it isn't, but if you can use it if you want >_< -->    <p>The worst paragraph ever.</p>  </body></html>"), ["h1", 
 "p"])
