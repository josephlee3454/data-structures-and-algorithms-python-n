class Node:

  def __init__(self):
    self.data = data # starts instance of data which is whats in the node 
    self.next_node = None # set the reference of next node to null

class LinkedList:

  def __init__(self):
    self.head = None # set the first instance of head node to null
    self.num_nodes = 0# start num of nodes to 0 so you can keep track of the nodes you create 


  def insert_start(self):
    self.num_nodes = self.num_nodes + 1 # adds to count since in this function you will create nodes for every time its ran it will add the appropriate nodes
    self.new_node = Node(data)# assigns the the data to new_node which will give you an instance of the the data for that perspective node
    
    if not self.head:
      self.head = new_node # if there is no head node we will create one by asssaigning the data to the new_node then assigning new_node to the head

    else:
      new_node.next_node =  self.head # sets the next node since you already have a head 
      self.head = new_node  # sets new head 

  def insertion_end(self,data):# define function pass in data and self
    self.num_nodes = self.num_nodes + 1 # add 1 to your nodes 
    new_node = Node(data)# assaign new_node to the represnt the data
    actual_node = self.head  # actual node now becomes the head node
    while actual_node.next_node is not None:# will continue to loop as long as there is nodes left to point to if no nodes left it will break out of the while loop 
      actual_node = actual_node.next_node# what we use to point at the next node 
    actual_node.next_node = new_node# this is what actually creates the new node at the end as long as your while loop condition is met 

  def size_of_linked_list(self):
    return self.num_nodes#call this function when you want the number of nodes thats why we add to this varible thoughout our functionality 

  def traverse(self):
    actual_node = self.head # assaign head to actual node 
    while actual node is not None:#this will ensure we are notat the end of the linked list 
    print(actual_node.data) # this prints the individual nodes DATA
    actual_node = actual_node.next_node # update actual node to the next node  

  



