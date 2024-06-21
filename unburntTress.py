def noOfUnburntTress(r,c):
    if r<0 or c<0 or r>=n or c>=n or matrix[r][c]!=1:
        return
    if matrix[r][c]==1:
        matrix[r][c]=2
    noOfUnburntTress(r-1,c)
    noOfUnburntTress(r,c-1)
    noOfUnburntTress(r+1,c)
    noOfUnburntTress(r,c+1)
n=int(input())
matrix=[]
for i in range(n):
    row=list(map(int,input().split(" ")))
    matrix.append(row)

r,c=map(int,input().split(" "))
noOfUnburntTress(r-1,c-1)
print(matrix)
c=0
for row in matrix:
    c+=row.count(1)
print(c)

