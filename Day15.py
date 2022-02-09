def merge(arr,left,mid,right):
    n1 = mid - left + 1
    n2 = right - mid
    a= [n1]
    b = [n2]
    for i in range(n1):
        a[i] = arr[left + i]
    for i in range(n2):
        b[i] = arr[mid + 1 + i]
    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if a[i] < b[j]:
            k += 1
            j += 1
        else:
            arr[k] = b[j]
            k += 1
            i += 1
    while i < n1:
        arr[k] = a[i]
        k += 1
        i += 1
    while i < n2:
        arr[k] = b[j]
        k += 1
        j += 1

def merge_sort(arr,left,right):
    if left < right:
        mid = (left + right)/2
        merge_sort(arr,left,mid)
        merge_sort(arr,mid+1,right)
        merge(arr,left,mid,right)

arr = [5,4,3,2,1]
merge_sort(arr,0,4)
print(arr)