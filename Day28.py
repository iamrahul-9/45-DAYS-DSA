# A class that represents an individual node in a
# Binary Tree
class Node:
    def __int__(self,data):
        self.left = None
        self.right = None
        self.key = data

# create root
root = Node(1)
''' following is the tree after above statement
        1
      /   \
     None  None'''

root.left = Node(2)
root.right = Node(3)
''' 2 and 3 become left and right children of 1
           1
         /   \
        2      3
     /    \    /  \
   None None None None'''

root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
'''4 and 5 becomes left child of 2 and 6 and 7 become right child of 3
           1
       /       \
      2          3
    /   \       /  \
   4     5     6    7
  /  \  /  \  /  \ /  \
 N    N N   N N   N N   N'''
