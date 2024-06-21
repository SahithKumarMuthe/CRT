def is_safe(board, row, col,x,y):
    if row==x or col==y:
        return False
    
    for i in range(row):
        if board[i][col] == 1:
            '''or board[i][col]==2'''
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(N,x,y):
    board = [[0 for _ in range(N)] for _ in range(N)]
    board[x][y]=2
    f,c=place_nqueens(board, 0,0,x,y) 
    print(c)
    #print_solution(board)

# def place_nqueens(board, row, col,x,y,max=0):

#     if row==len(board):
#         return True,max
    
#     for col in range(len(board[row])):
#         if is_safe(board, row, col,x,y):
#             max+=1
#             board[row][col] = 1
#             if row+1!=x:

#                 c,f=place_nqueens(board,row+1,0,x,y,max)
#             else:
#                 c,f=place_nqueens(board,row+2,0,x,y,max)

#             if c>max:
#                 max=c
#             if f:
#                 return f,max
#             board[row][col]=0   
#     return False,max

def place_nqueens(board, row, col,x,y,max=0):

    if row==len(board):
        return True,max
    
    for col in range(len(board[row])):
        if row!=x:
            if is_safe(board, row, col,x,y):
                max+=1
                board[row][col] = 1
                break
            
                c,f=place_nqueens(board,row+1,0,x,y,max)
            

                if c>max:
                    max=c
                if f:
                    return f,max
                board[row][col]=0
        else:
            c,f=place_nqueens(board,row+1,0,x,y,max)
            if c>max:
                max=c

           
    return False,max

def print_solution(board):
    N = len(board)
    c=0
    for i in range(len(board)):
        for j in range(N):
            print(board[i][j],end=" ")
            if board[i][j] == 1:
                c+=1
        print()
    print(f'max no of queens can be placed are : {c}')

n = int(input()) 
x,y=map(int,input().split())
solve_nqueens(n,x,y)