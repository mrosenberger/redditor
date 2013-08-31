from bs4 import BeautifulSoup

class PostNode:
    
    def __init__(self, text, score, parent, children=[]):
        self.text = text
        self.score = score
        self.children = children
        self.parent = parent

    def addChild(self, child):
        self.children.append(child)

    def getChildren(self):
        return self.children

f = open('pages/reddit-0.html', 'r')
dump = ''.join(f.readlines())
f.close()

soup = BeautifulSoup(dump)

for thing in soup.contents:
    print thing
