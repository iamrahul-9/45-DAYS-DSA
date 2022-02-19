class Stack:
    li = []
    def __init__(self):
        print("Stack Created")
    
    def push(self,element):
        self.li.append(element)

    def pop(self):
        self.li.pop()
    
    def top(self):
        print(self.li[-1])

    def empty(self):
        if self.li == []:
            print(True)
        print(False)
    
    def display(self):
        print(self.li)

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

