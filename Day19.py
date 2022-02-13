class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at tail
    def insert_tail(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            last = self.head
            while last.next != None:
                last = last.next
            last.next = new_node
    
    # Make the Cycle
    def make_cycle(self,pos):
        temp = self.head

        count = 1
        while temp.next != None:
            if count == pos:
                startNode = temp
            temp = temp.next
            count += 1
        temp.next = startNode
    
    # Detect the Cycle
    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return slow

    # Remove the cycle
    def remove_cycle(self):
        meet = self.detect_cycle()
        start = self.head
        while start.next != meet.next:
            start = start.next
            meet = meet.next
        meet.next = None
        
    
    def print_llist(self):
        if self.head == None:
            print("Linked List is empty")
        temp = self.head
        while temp != None:
            print(temp.data,end="->")
            temp = temp.next
        print("NULL")

if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_tail(1)
    llist.insert_tail(2)
    llist.insert_tail(3)
    llist.insert_tail(4)
    llist.insert_tail(5)
    llist.insert_tail(6)
    llist.insert_tail(7)
    llist.insert_tail(8)
    # Cycle is created from element value 3
    llist.make_cycle(3)
    llist.detect_cycle()
    llist.remove_cycle()
    llist.print_llist()

