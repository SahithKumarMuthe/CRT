class Node:
    def __init__(self, u):
        self.data = u
        self.nxt = None
        self.prev = None

class dll:
    def __init__(self):
        self.head = None
        self.tail = None

    def addback(self, x):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            t = Node(x)
            t.prev = self.tail
            self.tail.nxt = t
            self.tail = t

    def addfront(self, x):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            t = Node(x)
            t.nxt = self.head
            self.head.prev = t
            self.head = t

    def lin_search(self, x):
        t1 = self.head
        t2 = self.tail
        while t1 != t2 and t1 != t2.nxt:
            if t1.data == x or t2.data == x:
                print("Found")
                return
            t1 = t1.nxt
            t2 = t2.prev
        if t1 == t2 and t1.data == x:  # check the middle element if t1 and t2 meet
            print("Found")
        else:
            print("Not Found")

    def pal(self):
        t1 = self.head
        t2 = self.tail
        while t1 != t2 and t1 != t2.nxt:
            if t1.data != t2.data:
                print("Not a palindrome")
                return
            t1 = t1.nxt
            t2 = t2.prev
        print("Palindrome")
    def bin(self):
        s = self.head
        f = self.head
        while f is not None and f.nxt is not None:
            s = s.nxt
            f = f.nxt.nxt
        t = s
        while t is not None:
            print(t.data, end="->")
            t = t.nxt
        print("None")

        t = self.head
        while t.nxt != s:
            print(t.data, end="->")
            t = t.nxt
        print("None")
        f.nxt=self.head
        s.prev.nxt=None
        d1.display()

    def display(self):
        t = self.head
        while t is not None:
            print(t.data, end="->")
            t = t.nxt
        print("None")

d1 = dll()
d1.addback(10)
d1.addback(20)
d1.addback(30)
d1.addback(40)
d1.addback(50)
d1.addback(60)


d1.display()
#d1.pal()
d1.bin()
#d1.lin_search(15)