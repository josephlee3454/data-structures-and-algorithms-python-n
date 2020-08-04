class Node(object):
  def __init__(self, value):
    self.value = value
    self.left  = None 
    self.right = None 

class Binary_Tree(object):
  def __init__(self, root):
    self.root = Node(root)
# 1-2-5-6-4-7-8-
#         1
#       /    \
#      2       3
#    /   \   /   \
#   4     5 6      7 the intial set up
  def print_tree(self, traversal_type):
    if traversal_type == "preorder":
      return self.preorder_print(tree.root, "")
    elif traversal_type == "inorder":
      return self.inorder_print(tree.root, "")
    elif traversal_type == "postorder":
      return self.postorder_print(tree.root, "")
  # 1-2-5-6-4-7-8-
  def preorder_print(self, start, traversal):
    if start: 
      traversal += (str(start.value) + "-")
      traversal = self.preorder_print(start.left, traversal)
      traversal = self.preorder_print(start.right, traversal)
    return traversal 
  # 1-2-5-6-4-7-8-
  def inorder_print(self, start, traversal):
    if start:
      traversal = self.inorder_print(start.left, traversal)
      traversal += (str(start.value) + "-")
      traversal = self.inorder_print(start.right, traversal)
    return traversal

  #4-2-5-6-3-7-8-1-
  def postorder_print(self, start, traversal):
    if start:
      traversal = self.inorder_print(start.left, traversal)
      traversal = self.inorder_print(start.right, traversal)
      traversal += (str(start.value) + "-")
    return traversal

class Bst:
  def insert(root, node):
    if root is None:
      root = node
    fizz_buzz_replace()
    else:
      if root.val < node.val:
        if root.right is None:
          root.right = node
        else:
          insert(root.right, Node)
      else: 
        if root.left is None:
          root.left = none 
      else: 
        if root.left is None:
          root.left = node 
        else:
          insert(root.left, node)

  def fizz_buzz_replace(self):
    if node(val) % 3 == 0:
      node(val) = 'fizz'
    elif node(val)%5 == 0:
	    node(val) = 'buzz'
    elif node(val) % 3 == 0 and node(val)%5:
      node(val) = ‘fizz-buzz’
  return node val 




tree = Binary_Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)




print(tree.print_tree("postorder"))
