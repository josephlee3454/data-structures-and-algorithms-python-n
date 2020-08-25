def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i - 1
        temp = lst[i]
        while j >= 0 and temp < lst[j]:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j+1] = temp
    return lst

# lst = [8,4,23,42,16,15]
# lst = [4, 42, 15, 16, 22, 54]
# lst = [-1,7,-9,98,34,56]
# print(insertion_sort(lst))

if __name__ == "__main__":
    assert insertion_sort([8,4,23,42,16,15]) == [4, 8, 15, 16, 23, 42]
    assert insertion_sort([4, 42, 15, 16, 22, 54]) == [4, 15, 16, 22, 42, 54]
    assert insertion_sort([-1,7,-9,98,34,56]) == [-9, -1, 7, 34, 56, 98]





