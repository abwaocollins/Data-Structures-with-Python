
def merge_sort(lst):
    # we check the length of the list if it is greater than one we proceed to the recursion otherwise return it
    if len(lst) <= 1:
        return lst
    # get midoint of the list
    #  use python floor operation to divide the lenght of list
    midpoint = len(lst)//2

    # call the mergesort fuction on both the left and right side of the list

    right = merge_sort(lst[midpoint:])

    left = merge_sort(lst[:midpoint])

    i = j = 0

    sorted_list = []

    # pick the least of the values and append it  to the sorted list

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
# add to the sorted list the reamining part of values that were not appended
    sorted_list += left[i:]
    sorted_list += right[j:]


    return sorted_list

# A test to determine whether the algorithm works

test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

for arr in test_cases:
        print(merge_sort(arr))
        

