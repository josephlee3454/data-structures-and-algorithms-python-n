class Node:
  
  @classmethod
  def __init__(self, data , next_node=None):
    self.data = data
    self.next_node = next_node

  def __repr__ (self):
    return f"{self.data} : {self.next_node}"
  def __str__(self):
    return f"{self.data} -> {self.data} -> {self.data} -> null"

class LinkedList(Node):
  @classmethod
  def __init__(self, head=None):
    self.head = head
  # @staticmethod
  def __repr__(self):
    return f"{self.head}"
  # @staticmethod
  def __str__(self):
    return f"{self.head}"
  
  # @staticmethod
  def insert_node(self):
  
    new_node = Node(data)
    if not self.head:
      self.head = new_node
    
    else:
      new_node.next_node = self.head 
      self.head = new_node




# ll = LinkedList()
# ll.insert("a")
# ll.insert("b")
# ll.insert("c")
# ll.print_list()
if __name__ == "__main__":
  # print(Node('hello'))
  ll = LinkedList()
  print(ll.insert_node())
   
