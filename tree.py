class Node:
    def __init__(self,val) -> None:
        self.left=None
        self.right=None
        self.data=val
class BST:
    def __init__(self) -> None:
        self.root=None
    def addNode(self,root,val):
        if root is None:
            return Node(val)
        elif root.data>val:
            root.left=self.addNode(root.left,val)
        else:
            root.right=self.addNode(root.right,val)
        return root
    def inorder(self,root):
        if root is None:
            return 
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)
    def preorder(self,root,ans=[]):
        if root is None:
            return []
        ans+=[root.data]
        ans+=self.preorder(root.left)
        ans+=self.preorder(root.right)
        return ans
    def postorder(self,root,ans=[]):
        if root is None:
            return []
        ans+=self.postorder(root.left)
        ans+=self.postorder(root.right)
        ans+=[root.data]
        return ans
    def sum(self,root,s=0):
        if root is None:
            return 0
       
        return root.data+self.sum(root.left)+self.sum(root.right)
    def eosum(self,root,es=0,os=0,diff=0):
        if root is None:
            return (0,0,0)
        
        es,os,diff=self.eosum(root.left)
        e,o,d=self.eosum(root.right)
        es+=e
        os+=o
        diff-=d

        if root.data%2==0:
            es+=root.data
        else:
            os+=root.data
        return (es,os,abs(es-os))
    def eodiff(self,root):
        if root is None:
            return 0
        if root.data%2==0:
            return root.data+self.eodiff(root.left)+self.eodiff(root.right)
        else:
            return self.eodiff(root.left)+self.eodiff(root.right)-root.data
    def esum(self,root):
        if root is None:
            return 0
        if root.data%2==0:
            return root.data+self.esum(root.left)+self.esum(root.right)
        else:
            return self.esum(root.left)+self.esum(root.right)
    def osum(self,root):
        if root is None:
            return 0
        if root.data%2:
            return root.data+self.osum(root.left)+self.osum(root.right)
        else:
            return self.osum(root.left)+self.osum(root.right)
    def printleafnodes(self,root,c=0,s=0):
        if root.left is None and root.right is None:
            s+=root.data
            c+=1
            return (c,s) 
        if root.left:
            c,s=self.printleafnodes(root.left,c,s)
        if root.right:
            c,s=self.printleafnodes(root.right,c,s)
        if root.left is None and root.right is None:
            s+=root.data
            c+=1
            return (c,s)   

        return (c,s)
    def height(self,root,l=0,r=0):
        if root is None:
            return -1
        if root.left is None and root.right is None:
            return 0
        if root.left:
            l=1+self.height(root.left)
        if root.right:
            r=1+self.height(root.right)
        return max(l,r)
    def leftView(self,root,c=0,ans=[]):
        if root is None:
            return ans
        if c not in ans:
            print(root.data,end=" ")
            ans.append(c)

        ans=self.leftView(root.left,c+1,ans)
        ans=self.leftView(root.right,c+1,ans)
        return ans
    def rightView(self,root,c=0,ans=[]):
        if root is None:
            return ans
        if c not in ans:
            print(root.data,end=" ")
            ans.append(c)
        ans=self.rightView(root.right,c+1,ans)
        ans=self.rightView(root.left,c+1,ans)
        
        return ans
    def isBalancedTree(self,root):
        if root is None:
            return True
        return (self.height(root.left)-self.height(root.right))>=2 or (self.height(root.left)-self.height(root.right))<=-2
               
                
        if flag and root.left:
            flag=self.isBalancedTree(root.left)
        if flag and root.right:
            flag=self.isBalancedTree(root.right)
        return flag         
    '''def isBalancedTree(self,root,flag=True):
        if root is None:
            return True
        if flag:
            if (self.height(root.left)-self.height(root.right))>=2 or (self.height(root.left)-self.height(root.right))<=-2:
                flag=False
                
        if flag and root.left:
            flag=self.isBalancedTree(root.left)
        if flag and root.right:
            flag=self.isBalancedTree(root.right)
        return flag '''        
    def search(self,root,key):
        if root is None:
            return False
        if root.data==key:
            return True
        if key <root.data:
            return self.search(root.left,key)
        else:
            return self.search(root.right,key)
    def depth(self,root,key,d=0,flag=False):
        if root is None:
            return -1,False
        if root.data==key:
            print(d)
            flag=True
            return (d,flag)
        if not flag:
            if key<root.data:
                d,flag=self.depth(root.left,key,d+1,flag)
            else:
                d,flag=self.depth(root.right,key,d+1,flag)
        return (d,flag)          
    def mainTopView(self,root):
        queue=[(root,0)]
        d={0:root.data}
        while queue:
            node,c=queue.pop(0)
            if node.left is not None:
                queue.append((node.left,c-1))
            if node.right is not None:
                queue.append((node.right,c+1))
            if c not in d:
                d[c]=node.data
        return d
    def BottomView(self,root):
        d={}
        queue=[(root,0)]
        while queue:
            node,c=queue.pop(0)
            if node.left is not None:
                queue.append((node.left,c-1))
            if node.right is not None:
                queue.append((node.right,c+1))
            if c not in d:
                d[c]=[node.data]
            else:
                d[c].append(node.data)
        return d
    def verticalOrder(self,root):
        queue=[(root,0)]
        d={}
        while queue:
            node,c=queue.pop(0)
            if node.left is not None:
                queue.append((node.left,c-1))
            if node.right is not None:
                queue.append((node.right,c+1))
            if c not in d:
                d[c]=[node.data]
            else:
                d[c].append(node.data)
        return d
    def levelOrder(self,root):
        queue=[root] 
        while queue:
            node=queue.pop(0)
            print(node.data,end=" ")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)              
nodes=list(map(int,input(" tree nodes ").split(" ")))
tree=BST()
tree.root=Node(nodes[0])
for i in range(1,len(nodes)):
    tree.addNode(tree.root,nodes[i])
# print("Inorder")
# tree.inorder(tree.root)
# print("\n")
# print("sum: " ,tree.sum(tree.root))
# es,os,diff=tree.eosum(tree.root)
# print(f'even sum= {es},odd sum ={os},difference= {diff}')
# print("only even sum : ",tree.esum(tree.root))
# print("only odd sum : ",tree.osum(tree.root))
# print(f" Differense : {abs(tree.eodiff(tree.root))}")
# print(f"leaf nodes of tree are ")
# print(tree.printleafnodes(tree.root))
# print("height of the tree is : ",end=" ")
# print(tree.height(tree.root))
# print("Is tree balanced(True/False):",tree.isBalancedTree(tree.root))
# print(tree.search(tree.root,13))
# key=int(input(" key ? : "))
# print(f"depth of node {key} is ",tree.depth(tree.root,key))
print("\n")
print("Left View")
tree.leftView(tree.root)
print("\nRight View")
tree.rightView(tree.root)
print("\nTop View")
top=tree.mainTopView(tree.root)
key=list(top.keys())
key.sort()
ntop={i:top[i] for i in key}
print("\n"," ".join(map(str,ntop.values())))
print("\nBottom View")
bottom=tree.BottomView(tree.root)
Bottom_key=list(top.keys())
Bottom_key.sort()
B={i:top[i]for i in Bottom_key}
for n in B:
    print(bottom[n][-1],end=" ")
print("\nVertical Order")
vertical=tree.verticalOrder(tree.root)
vertical_key=list(top.keys())
vertical_key.sort()
nvertical={i:vertical[i]for i in vertical_key}
for n in vertical_key:
    print(nvertical[n])
print("Level Order Traversal")
tree.levelOrder(tree.root)