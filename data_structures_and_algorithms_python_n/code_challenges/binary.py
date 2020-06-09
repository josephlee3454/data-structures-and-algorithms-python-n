

def binary_search(): 
  data_list = [-1,1,2,3,4,5,7,7,8,9]
  low = 0
  high = len(data_list)-1
  search_key = int(input("pick a number to look for: "))
  x1 = str(search_key)
  x2 = -1
  while low <=  high:
    mid = (low + high)//2
    if search_key < data_list[mid]:
      high = (mid - 1)
    if search_key > data_list[mid]:
      low = (mid + 1)
  
    elif search_key == data_list[mid] or search_key == x2:
      print("your " + x1 + " number is here")
      break
    else: 
      print("your number isnt here")
      break
binary_search()
