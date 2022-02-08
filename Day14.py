def is_safe(arr,x,y,n):
    if x < n and y < n and arr[x][y] == 1:
        return True
    return False

def rat_in_maze(arr,x,y,n,sol_arr):
    # base case
    if x == n-1 and y == n-1:
        sol_arr[x][y] = 1
        return True

    if is_safe(arr,x,y,n):
        sol_arr[x][y] = 1
        if rat_in_maze(arr,x+1,y,n,sol_arr):
            return True
        if rat_in_maze(arr,x,y+1,n,sol_arr):
            return True
        # Backtracking
        sol_arr[x][y] = 0 
        return False
    return False

n = int(input())

# original matrix
matrix = []
for i in range(n):
    a = list(map(int,input().split()))
    matrix.append(a)

# Solution matrix
sol_matrix = [[0 for j in range(n)] for i in range(n)]

print()

# display solved matrix
if rat_in_maze(matrix,0,0,n,sol_matrix):
    for i in range(n):
        for j in range(n):
            print(sol_matrix[i][j],end=" ")
        print()

# The Maze
# 1 0 1 0 1
# 1 1 1 1 1
# 0 1 0 1 0
# 1 0 0 1 1
# 1 1 1 0 1