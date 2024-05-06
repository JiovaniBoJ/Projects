# This program uses the merge sort algorithm to order a list.

"""Doc String
 The merge sort algorithm should be used.
 Variable names for all the variables.
 Modify the merge sort algorithm.?@~@
 Create the required methods and functions.
 Sort all the string list by string length.
 Run the modified  merge sort algorithm."""

# This is the function for the merge sort algorithm.


def merge_sort_strings(string_list):
    if len(string_list) <= 1:
        return string_list

    mid = len(string_list)/2
    left_side = string_list[:mid]
    right_side = string_list[mid:]

    left_side = merge_sort_strings(left_side)
    right_side = merge_sort_strings(right_side)

    # These are the empty lists.
    merged = []
    left_index = 0
    right_index = 0

    # While loop to the left half of the string list.
    while left_index < len(left_side) and right_index < len(right_side):
        if len(left_side[left_index]) >= len(right_side[right_index]):
            merged.append(left_side[left_index])
            left_index += 1
        else:

            merged.append(right_side[right_index])
            right_side += 1

            merged.extend(left_side[left_index:])
            merged.append(right_side[right_index:])

            return merged
