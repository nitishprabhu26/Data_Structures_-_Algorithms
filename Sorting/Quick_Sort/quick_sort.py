# QuickSort:
# https://www.geeksforgeeks.org/quick-sort/
# https://youtu.be/5iSZ7mh_RAk

# QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.
# There are many different versions of quickSort that pick pivot in different ways:
# Always pick first element as pivot.
# Always pick last element as pivot (implemented below)
# Pick a random element as pivot.
# Pick median as pivot.

# The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot,
# put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater
# elements (greater than x) after x. All this should be done in linear time.


def partition(start, end, array):

    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]

    # This loop runs till start pointer crosses end pointer, and when it does we swap the pivot with element on end pointer
    while start < end:

        # Increment the start pointer till it finds an element greater than pivot
        while start < len(array) and array[start] <= pivot:
            start += 1

        # Decrement the end pointer till it finds an element less than pivot
        while array[end] > pivot:
            end -= 1

        # If start and end have not crossed each other, swap the numbers on start and end
        if(start < end):
            array[start], array[end] = array[end], array[start]

    # Swap pivot element with element on end pointer. This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]

    # Returning end pointer to divide the array into 2
    return end


def quick_sort(start, end, array):
    if (start < end):
        # p is partitioning index, array[p] is at right place
        p = partition(start, end, array)

        # Sort elements before partition and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)


# Driver code
array = [10, 7, 8, 9, 1, 5]
quick_sort(0, len(array) - 1, array)
print(f'Sorted array: {array}')

# For all test cases:
all_test_cases = [
    [11, 9, 29, 7, 2, 15, 28],
    [3, 7, 9, 11],
    [25, 22, 21, 10],
    [29, 15, 28],
    [],
    [6]
]

for elements in all_test_cases:
    quick_sort(0, len(elements) - 1, elements)
    print(f'Sorted array: {elements}')

