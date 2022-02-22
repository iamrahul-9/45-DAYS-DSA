import numpy as np

# Q1. Max Till i
def max_till_i(a,n):
    mx = -9999
    for i in range(n):
        if a[i] > mx:
            mx = a[i]
        print(mx)
        
# ==========OR==========
    '''mx = max(mx,a[i])
       print(mx)'''

# Q2. Sum of Subarray
def sum_of_subarray(a,n):
    for i in range(n):
        curr = 0
        for j in range(i,n):
            curr += a[j]
            print(curr)

# Q3. Longest Arithematic Subarray - Google Kickstart
def longest_arithemetic_subarray(a,n):
    ans = 2
    pd = a[1] - a[0]
    curr = 2
    for i in range(2,n):
        if pd == a[i] - a[i-1]:
            curr += 1
        else:
            pd = a[i] - a[i-1]
            curr = 2
        ans = max(ans,curr)
    return ans

# Q4. Record Breaker - Google Kickstart
def record_breaker(a,n):
    if n == 1:
        return 1
    ans = 0
    mx = -1
   
    for i in range(n):
        if a[i] > mx and a[i] > a[i+1]:
            ans += 1
        mx = max(mx,a[i])
    return ans

# creating a numpy array
li = []
size = int(input("Enter size: "))
for i in range(size):
    x = int(input("Element: "))
    li.append(x)
arr = np.array(li)

# max_till_i(arr,size)
# sum_of_subarray(arr,size)    
# print(longest_arithemetic_subarray(arr,size))
# print(record_breaker(arr,size))
