# Queue using stack
# 1. Two stack approach
class Queue:
    stack1 = []
    stack2 = []

    def push(self,x):
        self.stack1.append(x)
    
    def pop(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            print("Queue is empty")
            return -1
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1[-1])
                self.stack1.pop()
        top_val = self.stack2[-1]
        self.stack2.pop()
        return top_val
    
    def empty(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True
        return False

# Recursive Approach
class Queue2:
    stack = []
    def push(self,x):
        self.stack.append(x)

    def pop(self):
        # base case
        if len(self.stack) == 0:
            print("Queue is empty")
            return -1
        x = self.stack[-1]
        self.stack.pop()
        if len(self.stack) == 0:
            return x
        item = self.pop()
        self.stack.append(x)
        return item

if __name__ == "__main__":
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    print(q.pop())
    q.push(5)
    print(q.pop())
    print(q.pop()) 
    print(q.pop())
    print(q.pop())
    print(q.pop())
    q2 = Queue2()
    q2.push(1)
    q2.push(2)
    q2.push(3)
    q2.push(4)
    print(q2.pop())
    print(q2.pop())
    print(q2.pop())
    print(q2.pop())
    print(q2.pop()) 

