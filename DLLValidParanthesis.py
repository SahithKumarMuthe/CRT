class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None

class DLL:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    def addBack(self,x):
        if self.head is None:
            self.head=Node(x)
            self.tail=self.head
        else:
            self.tail.next=Node(x)
            self.tail.next.previous=self.tail
            self.tail=self.tail.next
    def isvalid(self):
        stack=[]
        temp=self.head
        c=0
        d={']':'[',')':'(','}':'{'}
        while temp is not None:
            c+=1
            if temp.data=='[' or temp.data=='{' or temp.data=='(':
                stack.append(temp.data)
            else:
                if stack.pop()!=d[temp.data]:
                    return c
            temp=temp.next       
        if len(stack)==0:
            return -1
        else:
            return c
        
s=input()
d=DLL()
for char in s:
    d.addBack(char)
print(d.isvalid())