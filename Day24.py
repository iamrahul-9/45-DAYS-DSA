def precedence(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

def infix_postfix(s):
    stack = []
    res = ""
    for i in s:
        if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
            res += i
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while len(stack) != 0 and stack[-1] != '(':
                res += stack[-1]
                stack.pop()
            if len(stack) != 0:
                stack.pop()
        else:
            while len(stack) != 0 and precedence(stack[-1]) > precedence(i):
                res += stack[-1]
                stack.pop()
            stack.append(i)
    
    while len(stack) != 0:
        res += stack[-1]
        stack.pop()
    
    return res

def infix_prefix(s):
    stack = []
    res = ""
    reverse_s = s[::-1]
    for i in reverse_s:
        if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
            res += i
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while len(stack) != 0 and stack[-1] != '(':
                res += stack[-1]
                stack.pop()
            if len(stack) != 0:
                stack.pop()
        else:
            while len(stack) != 0 and precedence(stack[-1]) > precedence(i):
                res += stack[-1]
                stack.pop()
            stack.append(i)
    
    while len(stack) != 0:
        res += stack[-1]
        stack.pop()
    
    return res[::-1]

if __name__ == "__main__":
    expression = "(a-b/c)*(a/k-l)"
    print(infix_postfix(expression))
    print(infix_prefix(expression))
