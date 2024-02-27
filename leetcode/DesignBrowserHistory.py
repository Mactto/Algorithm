class Node():
    def __init__(self, url='', next=None, prev=None):
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory(object):
    def __init__(self, homepage: str):
        self.head = self.tail = Node(url=homepage)
        print(None)
    
    def visit(self, url):
        self.tail.next = Node(url=url)
        temp = self.tail
        self.tail = self.tail.next
        self.tail.prev = temp
        
        print(None)

    def back(self, steps):
        for _ in range(steps):
            if self.tail.prev is None:
                break
            self.tail = self.tail.prev
        print(self.tail.url)

    def forward(self, steps):
        for _ in range(steps):
            if self.tail.prev is None:
                break
            self.tail = self.tail.next
        print(self.tail.url)
    
browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit('google.com')
browserHistory.visit('facebook.com')
browserHistory.visit('youtube.com')
browserHistory.back(1)
browserHistory.back(1)
browserHistory.forward(1)
browserHistory.visit('linkedin.com')
browserHistory.forward(2)
browserHistory.back(2)
browserHistory.back(7)

 