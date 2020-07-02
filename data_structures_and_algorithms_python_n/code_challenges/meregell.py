# class Node:
#   def __init__(self,node_data):
#     self.node_data = node_data
#     self.next = None
  
# class LinkedList:
  
#   def __init__(self):
#     self.head = None

#   def printList(self):
#     temp_node = self.head

#     while temp_node:
#       print(temp.data, ends="->")
#       temp_node = temp_node.next


#   def append_node(self,new_data):
#     new_node = Node(new_data)

#     if self.head is None:
#       self.head = new_node
#       return

#     current = self.head
  
#     while current.next:
#       current = current.next
#     current.next = new_node
  # def merge_lists(head1,head2):

  #   temp_node = None

  #   if head1 is None:
  #     return head2
      
  #   if head2 is None:
  #     return head1

  #   if head1.node_data <= head2.node_data:
  #     temp_node = head1
  #     temp_node.next = merge_lists(head1.next, head2)
    
  #   else: 
  #     temp_node = head2
  #     temp_node.next = LinkedList.merge_lists(head1, head2.next)

  #   return temp_node

# if __name__ == "__main__":
#     ##list 1
#     list1 = LinkedList()
#     list1.append_node(1)
#     list1.append_node(3)
#     print(list1.head.next.node_data)
    # list1.append_node(5)
    # list1.append_node(7)
  
##list 2
    # list2 = LinkedList()
    # list2.append_node(2)
    # list2.append_node(4)
    # list2.append_node(6)
    # list2.append_node(8)

    # list3 = LinkedList()

    # list3.head = LinkeLists.merge_lists(list1.head,list2.head)

    # print("Merged Linked List is :", ends="")
    # list3.printlist()

def merge_lists(self,Ll1,Ll2):
  cur1 = Ll1.head ##assigns current1 to head of Ll1 
  cur2 = Ll2.head ## assigns current2 to head of Ll2

      

