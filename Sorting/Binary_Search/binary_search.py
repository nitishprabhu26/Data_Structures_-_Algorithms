# Binary Search:
# https://www.geeksforgeeks.org/binary-search/
# this search algorithm takes advantage of a collection of elements that is already sorted by ignoring half of 
# the elements after just one comparison.

# Binary Search: Search a sorted array by repeatedly dividing the search interval in half. Begin with an 
# interval covering the whole array. If the value of the search key is less than the item in the middle of the 
# interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check 
# until the value is found or the interval is empty.

# Compare x with the middle element.
# If x matches with the middle element, we return the mid index.
# Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after 
# the mid element. Then we apply the algorithm again for the right half.
# Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the 
# left half.

# Linear Search:
# The time complexity of the above algorithm is O(n).

from util import time_it


@time_it
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1


@time_it
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1



# recursion

@time_it
def binary_search_recursive(arr, x, low, high):
    # Check base case
    if high >= low:
        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search_recursive(arr, x, low, mid - 1)

        # Else the element can only be present in right subarray
        else:
            return binary_search_recursive(arr, x, mid + 1, high)

    else:
        # Element is not present in the array
        return -1


if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    # numbers_list = [i for i in range(1000)]
    number_to_find = 24

    # index = linear_search(numbers_list, number_to_find)
    # index = binary_search(numbers_list, number_to_find)

    index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list)-1)
    print(f"Number found at index {index} using binary search")


# Time Complexiety: O(log n)
# Auxiliary Space: O(1) in case of iterative implementation. In the case of recursive implementation, O(log n) 
# recursion call stack space.
# Algorithmic Paradigm: Decrease and Conquer.
