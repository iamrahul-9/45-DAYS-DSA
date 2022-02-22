def quick_sort(arr,low,high):
    if low < high:
        partition_pos = partition(arr,low,high)
        quick_sort(arr,low,partition_pos-1)
        quick_sort(arr,partition_pos+1,high)

def partition(arr,low,high):
    i = low
    j = high - 1
    pivot = arr[high] # last element of the array

    while i < j:
        while i < high and arr[i] < pivot:
            i += 1
        while j > low and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
    if arr[i] > pivot:
        arr[i],arr[high] = arr[high],arr[i]
    
    return i

arr = [8,5,3,4,26,6,9,52]
quick_sort(arr,0,len(arr)-1)
print(arr)

print("Hello World")