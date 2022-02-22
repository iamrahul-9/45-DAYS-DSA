class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at Head
    def insert_head(self,value):
        new_node = Node(value)
        # New node->next is assigned as head
        new_node.next = self.head
        # If head is not NULL i.e the list is not empty than head->prev is assigned as new node
        if self.head != None:
            self.head.prev = new_node
        # Due to Node class constructor new head prev points to Null automatically
        # New node becomes the head
        self.head = new_node

    # Insert at Tail
    def insert_tail(self,value):
        if self.head == None:
            self.insert_head(value)
            return
        new_node = Node(value)
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node
        temp.prev = temp
    
    def delete_head(self):
        self.head = self.head.next
        self.head.prev = None

    def deletion(self,value):
        if self.head == None:
            return

        if self.head.data == value or self.head.next == None:
            self.delete_head()
            return

        temp = self.head
        while temp.next.data != value:
            temp = temp.next
            if self.head.data != value:
                print("Value is not available")
                return
        temp.prev.next = temp.next  
        if temp.next != None:
            temp.next.prev = temp.prev

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data,end=" ")
            temp = temp.next
        print()

dllist = LinkedList()
dllist.insert_tail(1)
dllist.insert_tail(2)
dllist.insert_tail(3)
dllist.insert_tail(4)
dllist.display()
dllist.deletion(2)
dllist.display()