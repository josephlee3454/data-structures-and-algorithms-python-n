class newNode: 
  
  def __init__(self, key): 
    self.key = key 
    self.left = self.right = None

  def printCommon(root1, root2): 
        

    s1 = [] 
    s2 = [] 
    
    while 1: 
            
       
    if root1: 
      s1.append(root1) 
      root1 = root1.left 

    elif root2: 
      s2.append(root2) 
      root2 = root2.left 

  
    elif len(s1) != 0 and len(s2) != 0: 
      root1 = s1[-1]  
      root2 = s2[-1]  
    
         
    if root1.key == root2.key: 
      print(root1.key, end = " ") 
      s1.pop(-1)  
      s2.pop(-1) 

   
      root1 = root1.right  
      root2 = root2.right 

    elif root1.key < root2.key: 
              
      s1.pop(-1) 
      root1 = root1.right  

    
      root2 = None
    elif root1.key > root2.key: 
        s2.pop(-1) 
        root2 = root2.right  
        root1 = None

    else: 
      break

  
  def inorder(root): 
    if root: 
      inorder(root.left)  
      print(root.key, end = " ") 
      inorder(root.right) 


  def insert(node, key): 
       
    if node == None: 
        return newNode(key)  

     
    if key < node.key:  
        node.left = insert(node.left, key)  
    elif key > node.key:  
        node.right = insert(node.right, key) 
          
   
    return node 


if __name__ == '__main__': 
      

  root1 = None
  root1 = insert(root1, 5)  
  root1 = insert(root1, 1)  
  root1 = insert(root1, 10)  
  root1 = insert(root1, 0)  
  root1 = insert(root1, 4)  
  root1 = insert(root1, 7)  
  root1 = insert(root1, 9)  

  # Create second tree as shown in example  
  root2 = None
  root2 = insert(root2, 10)  
  root2 = insert(root2, 7)  
  root2 = insert(root2, 20)  
  root2 = insert(root2, 4)  
  root2 = insert(root2, 9) 

  print("Tree 1 : ")  
  inorder(root1)  
  print() 
    
  print("Tree 2 : ") 
  inorder(root2) 
  print() 

  print("Common Nodes: ")  
  printCommon(root1, root2) 
