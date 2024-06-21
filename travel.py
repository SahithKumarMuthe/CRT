'''without obstacle'''
def travel(m,n,i,j,x,y,visited=[],c=0):
    if i==x and j==y:
        return 0
    if j>=m or i>=n or i<0 or j<0 :
        return 0
    if j==m-1 and i==n-1:
        visited.append((i,j))
        print(visited)
        visited.pop()
        return 1
    
    visited.append((i,j))
    if (i,j+1) not in visited:
        c+=travel(m,n,i,j+1,x,y,visited)
    if (i-1,j) not in visited:
        c+=travel(m,n,i-1,j,x,y,visited)
    if (i,j-1) not in visited:
        c+=travel(m,n,i,j-1,x,y,visited)
    if (i+1,j) not in visited:
        c+=travel(m,n,i+1,j,x,y,visited)
    visited.pop()
    
    return c

'''with obstacle'''
# def travel(i,j):
#     if j>=m or i>=n or path[i][j]!='_':
#         return 0
#     if j==m-1 and i==n-1:
#         return 1
#     return travel(i,j+1)+travel(i+1,j)

'''using DP'''
# def travel(i,j):
#     pass
    
dp=[]
path=[[0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]]
m=4
n=3
for i in range(n):
    dp.append([-1]*m)

   
print(travel(4,3,0,0,1,2))