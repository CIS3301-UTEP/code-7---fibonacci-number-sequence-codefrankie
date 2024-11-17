# def merge_sort(unsorted_list):
#     if len(unsorted_list) <= 1:
#         return unsorted_list
    
#     mid = len(unsorted_list) //2

#     left_half = merge_sort(unsorted_list[:mid])
#     right_half = merge_sort(unsorted_list[mid:])

#     return merge(left_half, right_half)

# def merge(left, right):
#     sorted_list = []
#     left_index = 0
#     right_index = 0

#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] < right[right_index]:
#             sorted_list.append(left[left_index])
#             left_index += 1
#         else:
#             sorted_list.append(right[right_index])
#             right_index += 1

#     sorted_list.append(left[left_index:])
#     sorted_list.extend(right[right_index])

#     return sorted_list

# merge([21,1,43,3,2,53,647,76,88,2,5])


def merge_sort(list_to_order):
    if len(list_to_order) <= 1:
        return list_to_order
    
    middle_point = len(list_to_order) // 2

    left_half = merge_sort(list_to_order[:middle_point])
    right_half = merge_sort(list_to_order[middle_point:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    sorted_list.extend(left[left_index])
    sorted_list.extend(right[right_index])

    return sorted_list

unsorted_list = [23,1,543,34,3,233,423,43,99,1,3,44,65,12]
print(unsorted_list)
result = merge_sort(unsorted_list)

print(result)