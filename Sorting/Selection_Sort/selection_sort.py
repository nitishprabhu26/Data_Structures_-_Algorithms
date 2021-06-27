# Selection Sort
# The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from
# unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
# 1) The subarray which is already sorted.
# 2) Remaining subarray which is unsorted.
# In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked
# and moved to the sorted subarray.

def selectionSort(arr):
    n = len(arr)

    for i in range(n-1):
        min_idx = i

        # Find the minimum element in remaining unsorted array
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element 
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Driver code to test above
arr = [64, 25, 12, 22, 11]
arr = [78, 12, 15, 8, 61, 53, 23, 27]

selectionSort(arr)
print("Sorted array is:")
print(arr)


# Time Complexity: O(n2) as there are two nested loops.
# Auxiliary Space: O(1)
# The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a
# costly operation.
# In Place : Yes, it does not require extra space.
