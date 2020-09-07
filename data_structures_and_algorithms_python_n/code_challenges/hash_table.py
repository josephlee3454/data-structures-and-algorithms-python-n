from data_structures_and_algorithms_python_n.code_challenges.htprac import LinkedList, Node


class HashTable:
  def __init__(self, size = 1024):
    self.size = size # instantiates the size of the hash table
    self._buckets = [None] * size 

  def _hash(self,key):
    hash_total = 0
    for ch in key:
      hash_total += ord(ch)

    return (hash_total*199) % self.size
  
  def add(self,key, value):
    hashed_key = self._hash(key)

    if not self._buckets[hashed_key]:
      self._buckets[hashed_key] = LinkedList()

    self._buckets[hashed_key].append([key,value])


  def get(self,key):
    hashed_key= self._hash(key)
    bucket = self._buckets[hashed_key]
    current = bcuket.head
    while current:
      if current.data[0] == key:
        return current.data[1]

  def contains(self,key):
    if key in self._buckets:
      return key(value)
    else:
      return "dosnt exsist"



HashTable.add(2,3)
HashTable.get(2)


   