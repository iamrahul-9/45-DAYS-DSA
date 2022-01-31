# print all subarray (Legacy Approch) 
def all_subarray(a,n):
    for i in range(n):
        for j in range(i,n+1):
            for k in range(i,j):
                print(a[k],end=" ")
            print()

# Max sum subarray O(n*2)
def max_subarray(a,n):
    maxSum = -1e6
    for i in range(n):
        for j in range(i,n+1):
            sum = 0
            for k in range(i,j):
                sum += a[k]
            maxSum = max(sum,maxSum)
    print(maxSum)

# Max sum subarray O(n)
def cum_sum_subarray(a,n):
    maxsum_so_far = a[0]
    curr_max = a[0]
    for i in range(1,n):
        curr_max = max(curr_max,curr_max + a[i])
        maxsum_so_far = max(maxsum_so_far,curr_max)
    print(maxsum_so_far)

# Pythonic way
def all_sub(a,n):
    for i in range(n):
        for j in range(i,n+1):
            print(a[i:j])

# array created
size = int(input("Size: "))
arr = list(map(int,input().split()))

# all_subarray(arr,size)
# all_sub(arr,size)
# max_subarray(arr,size)
cum_sum_subarray(arr,size)