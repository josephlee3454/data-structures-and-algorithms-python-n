class Node:


  def __init__(self, value):

    self.value = value
    self.next = None

  def __repr__ (self):

    return f"{self.value} : {self.next_node}"
  def __str__(self):

    return f"{self.value} -> {self.value} -> {self.value} -> null"

class LinkedList:

  def __init__(self):
    self.head = None
  
  def print_list(self):
    current_node = self.head
    while current_node:
      print(current_node.value)
      current_node = current_node.next
 
  def __repr__(self):
    return f"{self.head_node}:"
  
  def __str__(self):

    return f"{self} -> {self} -> {self} -> null"
  
  def insert(self,value):
    new_node = Node(value)

    if self.head is None:
      self.head = new_node
      return
    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node



ll = LinkedList()
ll.insert("a")
ll.insert("b")
ll.insert("c")
ll.print_list()
