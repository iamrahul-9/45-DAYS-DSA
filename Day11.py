# Q1. Lowercase and Uppercase
str = "nbdhjgGAjgUj"
# To get the ASCII code of a character, use the ord() function
# print(ord("n")-ord("N")) # The difference is 32
for i in str:
    if ord(i) >= ord('a') and ord(i) <= ord('z'):
        str2 = ord(i) - 32
        # To get the character encoded by an ASCII code number, use the chr() function.
        str2 = chr(str2)
        print(str2,end="")
    else:
        str2 = ord(i) + 32
        str2 = chr(str2)
        print(str2,end="")
print()

# Inbuild function
str = "hello"
print(str.upper())
str = "WORLD"
print(str.lower())

# Q2. Biggest number from the numeric string
str = "4698348"
strsort = sorted(str,reverse=True)
s = "".join(strsort)
print(s)

# Q3. Maximum number occuring in string
str = "manfbfaskajabhdkladma"
all_freq = {}
count = 0
for i in str:
    if i in all_freq:
        all_freq[i] += 1
        count += 1
    else:
        all_freq[i] = 1
res = max(all_freq,key = all_freq.get)
print(res,all_freq[res])