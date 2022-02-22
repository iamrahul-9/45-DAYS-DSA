def is_operand(c):
	"""
	Return True if the given char c is an operand, e.g. it is a number
	"""
	return c.isdigit()


def prefix_evaluation(expression):
	"""
	Evaluate a given expression in prefix notation.
	Asserts that the given expression is valid.
	"""
	stack = []

	# iterate over the string in reverse order
	for c in expression[::-1]:

		# push operand to stack
		if is_operand(c):
			stack.append(int(c))

		else:
			# pop values from stack can calculate the result
			# push the result onto the stack again
			o1 = stack.pop()
			o2 = stack.pop()

			if c == '+':
				stack.append(o1 + o2)

			elif c == '-':
				stack.append(o1 - o2)

			elif c == '*':
				stack.append(o1 * o2)

			elif c == '/':
				stack.append(o1 / o2)

			elif c == '^':
				stack.append(o1 ** o2)
			else:
				return "Wrong Expression"

	return stack.pop()
	
def postfix_evaluation(expression):
    stack = []
    for i in expression:
        if i >= '0' and i <= '9':
            stack.append(int(i))
        else:
            opt2 = stack.pop()
            opt1 = stack.pop()
        
            if i == '+':
                stack.append(opt1+opt2)
            elif i == '-':
                stack.append(opt1-opt2)
            elif i == '*':
                stack.append(opt1*opt2)
            elif i == '/':
                stack.append(opt1/opt2)
            elif i == '^':
                stack.append(opt1**opt2)
                
    return int(stack.pop())

if __name__ == "__main__":
	test_expression = "-+7*45+20"
	print(prefix_evaluation(test_expression))

	expression = "46+2/5*7+"
	print(postfix_evaluation(expression))