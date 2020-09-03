def quick_sort(arr, low, high):
	if low < high:
		p = partition(arr,low,high)
		quick_sort(arr, low , p-1)
		quick_sort(arr, p+1, high)
def partition(arr,low,high):
	i = (low -1)
	pivot = arr[high] // 2
	for j in range(low,high):
		if arr[j] < pivot: 
		  i = i + 1
		  arr[i],arr[j] = arr[j], arr[i]
	arr[i+1],arr[high ]= arr[high], arr[i+1]
	return (i+1)
# def get_pivot(arr,low,high):
# 	mid = (high + low) // 2
# 	pivot = high
# 	if arr[low] < arr[high]:
# 		if arr[mid] < arr[high]:
#       pivot = mid
# 	elif arr[low] = arr[high]:
# 		pivot = low 
# 	return pivot


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])

