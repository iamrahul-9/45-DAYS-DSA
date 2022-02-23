n = 20
class Queue:
    arr = [None] * n
    front = -1
    back = -1

    def __init__(self):
        print("Queue created")
    
    def enqueue(self,x):
        if self.back == n-1:
            print("Queue overflow")
            return
        self.back += 1
        self.arr[self.back] = x

        if self.front == -1:
            self.front += 1
    
    def dequeue(self):
        if self.front == -1 or self.front > self.back:
            print("No elements in queue")
            return
        self.front += 1
    
    def peek(self):
        if self.front == -1 or self.front > self.back:
            print("No elements in queue")
            return -1
        return self.arr[self.front]
    
    def empty(self):
        if self.front == -1 or self.front > self.back:
            return True
        return False

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print(queue.peek())
    queue.dequeue()
    print(queue.peek())
    queue.dequeue()
    print(queue.peek())
    queue.dequeue()
    print(queue.peek())
    queue.dequeue()

    print(queue.empty())

        
