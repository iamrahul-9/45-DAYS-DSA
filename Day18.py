class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            last = self.head
            while last.next != None:
                last = last.next
            last.next = new_node

    # Reverse a linked list
    def reverse(self):
        # We need 3 pointers 
        prev = None # Initialised as None
        curr = self.head # Initialised as head
        # loop until current pointer doesnt reach to None
        while curr != None:
            # next is created and intialised as next pointer of current
            next = curr.next
            # the three pointer are incremented
            curr.next = prev
            prev = curr
            curr = next
            # last node becomes the new head  
            self.head = prev

    def print_list(self):
        if self.head == None:
            print("Linked list is empty")
        temp = self.head
        while temp != None:
            print(temp.data,end="->")
            temp = temp.next
        print("NULL")

llist = LinkedList()
n = int(input("Enter the end limit: "))
for i in range(n):
    num = int(input(f"Element {i+1}: "))
    llist.insert_tail(num)

llist.print_list()
llist.reverse()
llist.print_list()