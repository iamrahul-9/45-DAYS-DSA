# Node Class
class Node:
    def __init__(self,data):
        # data -> the value which the node stores
        # next -> pointer of the next node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        # head -> instantiated when the linkedlist is called 
        self.head = None

    # Method to insert a new node at the end
    def insert_tail(self,value):
        # Allocate the Node & Put in the data
        new_node = Node(value)
        # If the Linked List is empty, then make the new node as head
        if self.head == None:
            self.head = new_node
        # Else traverse till the last node
        else:
            last = self.head
            while last.next != None:
                last = last.next
        # Change the next of last node
            last.next = new_node

    # Method to insert a new node at the beginning
    def insert_head(self,value):
        # Allocate the Node & Put in the data
        new_node = Node(value)
        # Make next of new Node as head
        new_node.next = self.head
        # Move the head to point to new Node
        self.head = new_node

    # Delete the first element
    def delete_head(self):
        if self.head == None:
            return
        else:
            # delete the first element
            self.head = self.head.next
    
    # Delete by key
    def delete_key(self,key):
        if self.head == None:
            return

        if self.head.next == None or self.head.data == key:
            self.delete_head()
            return

        temp = self.head
        while temp.next.data != key:
            temp = temp.next
        todelete = temp.next # saved the address of the element
        temp.next = temp.next.next
        # delete the element (although its not required becoz python manage the garbage collection)
        del todelete

    # Search and return the index value
    def search(self,key):
        temp = self.head
        i = 0
        while temp != None:
            if temp.data == key:
                return f"The element {key} is present at {i} index."
            temp = temp.next
            i += 1
        return f"Oops!,element {key} is not in the linked list"

    # Traverse the Linked list to print the elements
    def print_list(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp != None:
                print(temp.data,end="->")
                temp = temp.next
            print("NULL")

llist = LinkedList()

n = int(input("Enter the length of linked list: "))
for i in range(n):
    x = int(input(f"Element {i+1}: "))
    llist.insert_tail(x)

llist.print_list()
# llist.delete_head()
# llist.insert_head(int(input("Enter no: ")))
# print(llist.search(int(input("Search: "))))
llist.delete_key(int(input()))
llist.print_list()