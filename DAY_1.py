def sum(n):
    if (n <= 0):
        return 0
    return n + sum(n-1)

# print(sum(int(input())))

def fact(n):
    if n == 1:
        print(n)
        return 1
    else:
        print(n,"*",end=" ")
        return n * fact(n-1)

print(fact(7))


