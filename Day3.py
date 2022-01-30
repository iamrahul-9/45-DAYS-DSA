import numpy as np

# Selection Sort - O(n*2)
def selection_sort(arr,n):
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[j] < arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    return arr

# Bubble Sort - O(n*2)
def bubble_sort(arr,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                # 🐍 pythonic way to swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Insertion Sort - Worst and Average Case O(n*2), Best Case Ω(n) 
def insertion_sort(arr,n):
    for i in range(1,n):
        current = arr[i]
        j = i-1
        while j>=0 and current<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current
    return arr

# Numpy array created using list and numpy
li = []
size = int(input("Enter Size: "))
for i in range(size):
    x = int(input("Element: "))
    li.append(x)
arr = np.array(li)

# Functions are been called
print(selection_sort(arr,size))
print(bubble_sort(arr,size))
print(insertion_sort(arr,size))
