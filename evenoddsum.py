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
    def evenOddSum(self,l,e_sum,o_sum):
        if l is None:
            return abs(e_sum-o_sum)
        elif l.data%2==0:
            e_sum+=l.data
            return self.evenOddSum(l.next,e_sum,o_sum)
        else:
            o_sum+=l.data
            return self.evenOddSum(l.next,e_sum,o_sum)
        
s=list(map(int,input().split(",")))
d=DLL()
for num in s:
    d.addBack(num)
print(d.evenOddSum(d.head,0,0))