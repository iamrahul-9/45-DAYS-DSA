# Two-Dimensional Array
# Searching in matrix
def search_matrix(a, n, m):
    k = int(input("Enter a number to search in matrix: "))
    x = y = None
    flag = False
    for i in range(n):
        for j in range(m):
            if a[i][j] == k:
                x, y = i, j
                flag = True
    if flag:
        print(f"Element {k} is found at {x,y}")
    else:
        print(f"Element {k} is not in the matrix")

# Spiral Order Matrix Traversal


def spiral_order(a, n, m):
    row_start, row_end, col_start, col_end = 0, n-1, 0, m-1
    while (row_start <= row_end) and (col_start <= col_end):

        # For row_start
        for col in range(col_start, col_end+1):
            print(a[row_start][col], end=" ")
        row_start += 1

        # For col_end
        for row in range(row_start, row_end+1):
            print(a[row][col_end], end=" ")
        col_end -= 1

        # For row_end
        for col in range(col_end, col_start-1, -1):
            print(a[row_end][col], end=" ")
        row_end -= 1

        # For col_start
        for row in range(row_end, row_start-1, -1):
            print(a[row][col_start], end=" ")
        col_start += 1


# Declaration
matrix = []  # Outer array of the matrix
n = int(input("Enter Rows: "))
m = int(input("Enter Columns: "))
for i in range(n):
    a = []  # inner array of the matrix
    for j in range(m):
        num = int(input("Enter Number: "))
        a.append(num)
    matrix.append(a)

# Printing the matrix
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end="   ")
    print()

print("-"*20)

# search_matrix(matrix,n,m)
spiral_order(matrix, n, m)
