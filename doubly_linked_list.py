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
    
    def addFront(self,x):
        if self.head is None:
            self.head=Node(x)
            self.tail=self.head
        else:
            self.head.previous=Node(x)
            self.head.previous.next=self.head
            self.head=self.head.previous

    def addMiddle(self,x,y):
        if self.head is None:
            self.head=Node(x)
            self.tail=self.head
        else:
            temp=self.head
            while temp.data!=y:
                temp=temp.next
            t=Node(x)
            t.next=temp.next
            t.previous=temp
            temp.next.previous=t
            temp.next=t

    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        print("\n")
    def rev_display(self):
        temp=self.tail
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.previous
        print("\n")
    def search(self,key):
        temp1=self.head
        temp2=self.tail
        
        while temp1!=temp2.next:
            print(temp1.data,temp2.data)
            if temp1.data==key or temp2.data==key:
                print("found")
                break
            temp1=temp1.next
            temp2=temp2.previous
        else:
            if temp1.data==key:
                print("found")
            else:
                print("Not found")

    def length(self):
        temp1=self.head
        temp2=self.tail
        t1_length=0
        while (temp1!=temp2.next and temp1!=temp2):
            t1_length+=1
            temp1=temp1.next
            temp2=temp2.previous
        
        if temp1==temp2:
            print("odd")
            print(t1_length*2+1)
        else:
            print("even")
            print(t1_length*2)
        
    def ispalindromic(self):
        temp1=self.head
        temp2=self.tail
        
        while (temp1!=temp2.next and temp1!=temp2):
            if temp1.data!=temp2.data:
                print("Not a palindrome")
                break
            temp1=temp1.next
            temp2=temp2.previous
        else:
            print("palindrome")

    def modify(self):
        temp1=self.head
        temp2=self.tail
        while (temp1!=temp2.next):
            temp1=temp1.next
            temp2=temp2.previous
        # temp2=temp2.next
        # temp3=self.head
        # while temp2 is not None:
        #     temp3.data,temp2.data=temp2.data,temp3.data
        #     temp3=temp3.next
        #     temp2=temp2.next
        self.tail.next=self.head
        self.head.previous=self.tail
        temp2.next=None
        temp1.previous=None
        self.tail=temp2
        self.head=temp1   

    def swap(self):
        p=current=self.head
        n=self.head.next
        self.head=self.head.next
        while current is not None and current.next is not None:
            current.next=current.next
            n.next=p
            n.previous=p.previous
            current.previous=n
            p.next=n
            current,p=p,current
            p=next
            current=current.next.next
            n=n.next.next

       
s=input()
d=DLL()
for char in s:
    d.addBack(char)
print(d.isvalid())
# d=DLL()
# d.addBack(1)
# d.addBack(2)
# d.addBack(3)
# d.addBack(4)
# d.addBack(5)
# d.addBack(6)
# d.addBack(7)
# d.addBack(8)
# d.addBack(9)
# d.addBack(10)
# d.display()
# d.rev_display()
# d.search(7)
# d.length()
# d.ispalindromic()
# d.swap()
# d.display()


            


