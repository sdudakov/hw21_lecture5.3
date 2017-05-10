from collections import deque
linked_list = deque([1, 2, 3, 4, 5,])


def reverse(linked_list):
    temp_list = []
    linked_list_reversed = deque([])
    for element in linked_list:
        temp_list.append(element)
    linked_list_reversed = temp_list[::-1]
    return linked_list_reversed

print(reverse(linked_list))
