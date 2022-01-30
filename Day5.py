# Q1. First repeating element
def first_repeating_element(a,n):
    min = -1
    for i in range(n):
        if a.count(a[i])>1:
            min = i
            break
    print(min+1) # Because we are showing index from 1 as an ans

# Q2. Subarray with given sum
def subarray_given_sum(a,n):
    s = int(input("Enter Sum: "))
    i,j,st,en,sum = 0,0,-1,-1,0
    
    while(j < n and sum + a[j] <= s):
        sum += a[j]
        j += 1

    if sum == s:
        print(i+1,j)
        return
    
    while j < n:
        sum += a[j]
        while sum > s:
            sum -= a[i]
            i += 1
        
        if sum == s:
            st = i+1
            en = j+1
            break
        j += 1
    print(st,en)

# Q3. Smallest positive missing number (Incomplete)
def smallest_positive_array(a,n):
    N = 999
    check = []
    for i in range(N):
        check[i] = False
    for i in range(n):
        if a[i] >= 0:
            check[a[i]] = True
    
    ans = -1
    for i in range(1,N):
        if check[i] == False:
            ans = i
            break
    print(ans)

# creating the array
n = int(input("Size: "))
a = list(map(int,input().split()))

# first_repeating_element(a,n)
# subarray_given_sum(a,n)
# smallest_positive_array(a,n)
