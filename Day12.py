# Q1. Sum till n
def sum(n):
    if n == 0:
        return 0
    pre_sum = sum(n-1)
    return n + pre_sum

# Q2. n raised to p
def power(n,p):
    if p == 0:
        return 1
    prev_p = power(n,p-1)
    return n * prev_p

# Q3. Factorial
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

# Q4. Fibonacci number
def fib(n):
    if n == 1 or n == 0: # base condition
        return n
    return fib(n-1) + fib(n-2)

# Q5. Check if array is sored or not
def sorted(a,n):
    if n == 1:
        return True
    rest_array = sorted(a,n-1)
    return a[0] <= a[1] and rest_array
    # (or) rest_array = sorted(a[1:])
    # return a[n-1] >= a[n-2] and rest_array

# Q6. Print number till n
def num_dec(n):
    if n == 0:
        print(n)
        return
    print(n)
    num_dec(n-1)

def num_inc(n):
    if n == 0:
        print(n)
        return
    num_inc(n-1)
    print(n)


# print(sum(int(input())))

# n = int(input("Enter value of n: "))
# p = int(input("Enter value of p: "))
# print(power(n,p))

# print(fact(5))
# print(fib(10))

# arr = [1,2,9,4,5,6]
# n = len(arr)
# print(sorted(arr,n))

# num_dec(5)
# num_inc(5)

# Q7. First & Last Occurence of a number in an array
def first_occ(arr,n,i,key):
    # base condtion
    if i == n:
        return -1

    if arr[i] == key:
        return i
    return first_occ(arr,n,i+1,key)
    
def last_occ(arr,n,i,key):
    # base condition
    if i == n:
        return -1

    rest_array = last_occ(arr,n,i+1,key)
    if rest_array != -1:
        return rest_array
    
    if arr[i] == key:
        return i
    return -1

arr = [4,2,1,2,5,2,7]
n = len(arr)
key = int(input("Enter the number to search: "))

print(first_occ(arr,n,0,key))
print(last_occ(arr,n,0,key))