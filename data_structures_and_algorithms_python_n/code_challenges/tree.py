class Node:
  def __init__(self, val=None):
    self.val = val
    self.left  = None 
    self.right = None 

class BST:
  def __init__(self):
    self.root = None 
# 1-2-5-6-4-7-8-
#         1
#       /    \
#      2       3
#    /   \   /   \
#   4     5 6      7 the intial set up
def insert(self,val):
  if self.root == None:
    self.root=node(val)
  else: 
    self._insert(val,self.root)

def _insert(self, val, curr_node):
  if val < curr_node.val:
    if curr_node.left == None:
      cur_node .left = Node(val)
    else:
      self._insert(val,curr_node.left)
  elif val > cur_node.val:
    if cur_node.right==None:
      cur_node.right=Node(val)
    else:
      self._insert(val,cur_node.right)
  else:
    print("the node is already in tree")


  def print_bst(self):
    if self.root != None:
      self._print_tree(self.root)
  
  def _print_bst(self,curr_node):
    if curr_node != None:
      self._print_bst (curr_node.left)
      print(str(curr_node.value))
      self._print_bst (curr_node.right)

    
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

  def fill_tree(tree,num_elems=100,Max_int=1000):
    from random import randint 
    for _ in range(nums_elems):
      curr_elem = randint(0,max_int)
      tree.insert(curr_elem)
    return tree


tree = BST()
tree = fill_tree(tree)
tree.print_tree()




