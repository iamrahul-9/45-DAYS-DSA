# arr = "apple"
# for i in arr:
#     print(i)

# Q1. Check Palindrome
def check_palindrome(arr):
    flag = True
    n = len(arr)-1
    for i in range(n):
        if arr[i] != arr[n-i]:
            flag = False
            break

    if flag == True:
        print("Palindrome")
    else:
        print("Not Palindrome")

# Q2. Largest word in a sentence
def largest_word(arr):
    currLen,maxLen,st,maxst = 0,0,0,0
    n = len(arr)
    for i in range(n-1):
        if arr[i] == " ":
            if currLen > maxLen:
                maxLen = currLen
                maxst = st
            currLen = 0
            st = i+1
        else:
            currLen += 1
        
    print(maxLen)
    for i in range(maxLen):
        print(arr[i+maxst],end="")
        

arr = input("Enter the character arr: ")
# check_palindrome(arr)
largest_word(arr)