# print all subarray (Legacy Approch) 
def all_subarray(a,n):
    for i in range(n):
        for j in range(i,n+1):
            for k in range(i,j):
                print(a[k],end=" ")
            print()

# Pythonic way
def all_sub(a,n):
    for i in range(n):
        for j in range(i,n+1):
            print(a[i:j])

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

# maximum contiguous subarray O(n)
def maxSubArraySum(a,size):
    max_so_far =a[0]
    curr_max = a[0]
    for i in range(1,size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)
    print(max_so_far) 

# Kadane's Algorithm O(n)
def kedane_algo(a,n):
    curr_sum = 0
    max_sum = -1e6
    for i in range(n):
        curr_sum += a[i]
        if curr_sum < 0:
            curr_sum = 0
        max_sum = max(max_sum,curr_sum)
    return max_sum

# Circular Subarray Max Sum O(n)
def circular_max_subarray(arr,size):
    nonwrapsum = kedane_algo(arr,size)
    total_sum = 0
    for i in range(size):
        total_sum += arr[i]
        arr[i] = -arr[i]
    wrapsum = total_sum + kedane_algo(arr,size)
    print(max(wrapsum,nonwrapsum))

# Pair Sum Problem O(n*2)
k = int(input("Enter the value of K: "))
def pairsum(a,n,k):
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i]+a[j] == k:
                print(i,j)
                return True
    return False

# optimized using 2 pointer approach O(n)
def pair_sum(a,n,k):
    low = 0
    high = n-1
    while low < high:
        if a[low]+a[high] == k:
            print(low,high)
            return True
        elif a[low]+a[high] > k:
            high -= 1
        else:
            low += 1
    return False

# array created
size = int(input("Size: "))
arr = list(map(int,input().split()))

# all_subarray(arr,size)
# all_sub(arr,size)
# max_subarray(arr,size)
# cum_sum_subarray(arr,size)
# maxSubArraySum(arr,size)
# kedane_algo(arr,size)
# circular_max_subarray(arr,size)
# print(pairsum(arr,size,k))
print(pair_sum(arr,size,k))
