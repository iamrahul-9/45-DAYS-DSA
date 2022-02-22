class Stack:
    li = []
    def __init__(self):
        print("Stack Created")
    
    def push(self,element):
        self.li.append(element)

    def pop(self):
        self.li.pop()
    
    def top(self):
        return self.li[-1]

    def empty(self):
        if len(self.li) == 0:
            return True
        return False
    
    def display(self):
        return self.li

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.display()
    stack.pop()
    stack.pop()
    stack.display()
    stack.empty()
    stack.top()

