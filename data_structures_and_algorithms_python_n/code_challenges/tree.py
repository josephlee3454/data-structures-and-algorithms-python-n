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
    elif traversal_type == "max":
      return self.findMaxRecursive(root)
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

maxData = float("-infinity")
def find_max(root):    # maxData is the initially the value of root
	global maxData
	if not root:	
		return maxData
	if root.getData() > maxData:
		maxData = root.value
	find_max(root.left)
	find_max(root.right)
	return maxData
    
 






tree = Binary_Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(tree.print_tree("Max"))
