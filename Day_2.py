# Array
import numpy as np

li = []
for i in range(int(input("Enter the size of array: "))):
    x = input(f"Element {i}: ")
    li.append(int(x))

# numpy array created
arr = np.array(li)

# 1. min and max of array
max = arr[0]
min = arr[0]

for i in arr:
    if i > max:
        max = i

    if i < min:
        min = i

print(f"Min: {min}, Max: {max}")


# 2. sum of an array
sum = 0
for i in arr:
    sum += i

print(f"Sum of array = {sum}")

# 3.
li = []
print("Kids with the greatest number of candies")
for i in range(5):
    kids = int(input(f"kid {i+1}: "))
    li.append(kids)

arr2 = np.array(li)
max = 0

for i in range(5):
    if arr2[i] > max:
        max = arr2[i]
        kid = i
    

print(f"Kid {kid+1} have the maximum with {max} candies.")

# Linear search with array (Time Complexity: O(n))
def linear_search(arr,size,key):
    for i in range(size):
        if arr[i] == key:
            return i
    return -1

li = []
size = int(input("Enter Size: "))
for i in range(size):
    x = int(input(f"Element {i+1}: "))
    li.append(x)

arr = np.array(li)
key = int(input("Enter the key to search: "))

print(linear_search(arr,size,key))


# Binary Search with Array (Time Complexity: O(logn))
def binary_search(arr,size,key):
    low = 0
    high = size - 1
    while low <= high:
        mid = int((low+high)/2)
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1

li = []
size = int(input("Enter Size: "))
for i in range(size):
    x = int(input(f"Element {i+1}: "))
    li.append(x)

arr = np.array(li)
key = int(input("Enter the key to search: "))

print(binary_search(arr,size,key))