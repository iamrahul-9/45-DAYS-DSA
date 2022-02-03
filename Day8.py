import numpy as np
# # Matrix created
# matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])

# # Original Matrix
# for i in matrix:
#     print(i)

# # Transpose Matrix
# res = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
# print()
# for i in res:
#     print(i)

def multi_mat(m1,m2,n1,n2,n3):
    print("-"*10)
    ans = np.zeros([n1,n3])
    for i in range(n1):
        for j in range(n3):
            for k in range(n2):
                ans[i][j] += m1[i][k]*m2[k][j]
    
    for i in range(n1):
        for j in range(n3):
            print(ans[i][j],end="  ")
        print()

m1 = [] # Outer array of the matrix
m2 = []
n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))

for i in range(n1):
    a = [] # inner array of the matrix
    for j in range(n2):
        num = int(input("Enter Number: "))
        a.append(num)
    m1.append(a)
    mt1 = np.array(m1)

for i in range(n2):
    a = [] # inner array of the matrix
    for j in range(n3):
        num = int(input("Enter Number: "))
        a.append(num)
    m2.append(a)
    mt2 = np.array(m2)

# Printing the matrix
for i in range(n1):
    for j in range(n2):
        print(m1[i][j],end="   ")
    print()

print("-"*10)

for i in range(n2):
    for j in range(n3):
        print(m2[i][j],end="   ")
    print()

multi_mat(mt1,mt2,n1,n2,n3)

