# The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the 
# correct position in the sorted part.

# Function to do insertion sort
def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)

# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
# Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order. And it takes minimum time (Order of n) when elements are already sorted.
# Algorithmic Paradigm: Incremental Approach
# Sorting In Place: Yes
# Uses: Insertion sort is used when number of elements is small. It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.
