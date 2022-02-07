# Q1. Reverse a string
def reverse(s):
    # base condition
    if len(s) == 0:
        return
    # Step 1: Calling the string recursivly till end
    rest_string = s[1:]
    reverse(rest_string)
    # Step 2: Printing the first element
    print(s[0],end="")

# Q2. Replace pi with 3.14
def replacepi(s):
    # base case
    if len(s) == 0:
        return
    # recursive case
    if s[0] == "p" and s[1] == "i":
        print("3.14",end="")
        replacepi(s[2:])
    else:
        print(s[0],end="")
        replacepi(s[1:])

# Q3. Tower of Hanoi
def tower_of_hanoi(n,src,dest,helper):
    # base case
    if n == 0:
        return
    # recursive case
    tower_of_hanoi(n-1,src,helper,dest)
    print(f"Move from {src} to {dest}")
    tower_of_hanoi(n-1,helper,dest,src)

# Q4. Remove Duplicates
def remove_dup(s):
    # base case
    if len(s) == 0 or len(s) == 1:
        return s
    # recursive case
    ch = s[0]
    ans = remove_dup(s[1:])
    if ch == ans[0]:
        return ans
    return ch+ans 

# reverse("rahul")

# print()
# replacepi("pippxxppiixipi")

# print()
# tower_of_hanoi(2,'A','C','B') 

print(remove_dup("aaaabbbeeecddd"))