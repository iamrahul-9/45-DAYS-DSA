# Concatenation
str1 = "fam"
str2 = "ily"
str3 = "".join([str1, str2])
print(str3)
# or
print(str1+str2)

# clear
str3 = ""
# or
print(str3)

# Compare
if str1 is str2:
    # or str1 == str2
    print("Same")
else:
    print("Not same")

# empty
if not str3:  # If you know the data type is string
    # or str1 !="": If your variable could also be some other type
    print("empty")

# remove somthing from string
s1 = "nincompoop"
# s2 = s1[:3] + s1[6:]
# or
s2 = s1.replace("com", "")
print(s1.replace("com", ""))

# find
print(s1.find("com"))  # It returns the index value of first character find

# insert
line = "Kung Panda"
i = line.find("Panda")
line2 = "fu "
ans = line[:i]+line2+line[i:]
print(ans)

# len()
str = "hello world"
print(len(str))

# substring using slice
print(s1[6:])

# sort a string
a = "xzvgfdlajdh"
a1 = "".join(sorted(a))  # convert the sorted list into string
print(a1)
