class ListNode(object):
    def __init__ (self, prev= None, next=None, val=0):
        self.prev = prev
        self.next = next
        self.val = val

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = self.curr = ListNode(val=homepage)

    def visit(self, url: str) -> None:
        self.curr.next = ListNode(val=url, prev=self.curr)
        self.curr = self.curr.next
        return None
        

    def back(self, steps: int) -> str:
        while(steps > 0 and self.curr.prev != None):
            steps -= 1
            self.curr = self.curr.prev
        return self.curr.val

    def forward(self, steps: int) -> str:
        while(steps > 0 and self.curr.next != None):
            steps -= 1
            self.curr = self.curr.next
        return self.curr.val
    

#array list로 풀이
class ListNode(object):
    def __init__ (self, next=None, val=0):
        self.next = next
        self.val = val

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = self.curr = ListNode(val=homepage)

    def visit(self, url: str) -> None:
        self.curr.next = ListNode(val=url, prev=self.curr)
        self.curr = self.curr.next
        return None
        

    def back(self, steps: int) -> str:
        while(steps > 0 and self.curr.prev != None):
            steps -= 1
            self.curr = self.curr.prev
        return self.curr.val

    def forward(self, steps: int) -> str:
        while(steps > 0 and self.curr.next != None):
            steps -= 1
            self.curr = self.curr.next
        return self.curr.val