def merge_sorted(list)
  n = list.length 
  if n > 1:
    mid = n//2
    left = list[0:mid]
    right = list[mid:n]
    merge_sort(left)
    merge_sort(right)
    merge(left,right,list)


def merge(left,right,list):
  i = 0 
  j = 0 
  k = 0
  while i < left.length and j < right.length:
    if left[i] <= right[j]:
      list[k] = left[i]
      i = i + 1
    else:
      list[k] = right[j]
      j = j + 1
  
    k = k+1

  if i = left.length


  
