class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

class Stack:
  
  def __init__(self,top):
    self.top = None
  
  def __str__(self):
    return f"the top is {self.top}"
  
  def push(self, value):
    self.top = Node(value, self.top)


  def pop(self):
    if self.top:
      wanted = self.top
      wanted.next_node = None 
      self.top = self.top.next_node
      return wanted.value

  def isEmpty(self):
    if sefl.top is None:
      return True
    else:
      return False

  def peek(self):
    if self.top is None:
      raise AttributeError('the top of stack is empty')
    else:
      return self.top.value

class Queue:
  def __init__(self):
    self.queue = []

  def is_empty(self):
    return self.queue == []

  def enqueue(self,data):
    self.queue.append(data)

  def dequeue(self):
    data = self.queue[0]
    del self.queue[0]
    return data
  
  def peek(self):
    return self.queue[0]

  def size_queue(self):
    return len(self.queue)

queue = Queue

q  = Queue()
# print(q.is_empty())
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.size_queue())
print("Dequeue: ", q.dequeue())
print("Dequeue: ", q.dequeue())
print(q.size_queue())
# print("\n")
# q.printqueue()

