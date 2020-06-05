data_list = []
def fill_array():

  x = "quit"
  loop_cycle = True
  while loop_cycle == True:
    user_input_list = input("please enter what you would like in your list:")
    if user_input_list == x:
      loop_cycle = False
      return data_list
    elif user_input_list != x:
      data_list.append(user_input_list)
      print(data_list)

fill_array()
search_key = 0
def user_search_key():
 search_key = input("please enter what you are looking for: ")
 return search_key
user_search_key()

def binary_search(data_list, search_key): 
  low = 0
  high = len(data_list)-1
  while low <=  high:
    mid = low + high//2
  if search_key == data_list[mid]:
    return true
  elif search_key < data[mid]:
    high = mid - 1
  else:
      low = high +1
print(mid)

binary_search(data_list, search_key)



# def binary_search (data_list, search_key):
#   search_key = int(input("please enter number that you would like to search for "))