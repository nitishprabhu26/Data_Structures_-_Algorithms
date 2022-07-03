# Merge Sort:
# Merge Sort is a Divide and Conquer algorithm, Recursive algorithm. It divides the input array into two 
# halves, calls itself for the two halves, and then merges the two sorted halves.
# https://www.youtube.com/watch?v=TzeBrDU-JaY
# https://www.geeksforgeeks.org/merge-sort/


def mergeSort(arr):
    if len(arr) < 2:
        return

    # Finding the mid of the array
    mid = len(arr)//2

    # Dividing the array elements
    L = arr[:mid]

    # into 2 halves
    R = arr[mid:]

    # Sorting the first half
    mergeSort(L)

    # Sorting the second half
    mergeSort(R)

    i = j = k = 0

    # Copy data to temp arrays L[] and R[]
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


# OR
# https://youtu.be/nCNfu_zNhyI


def mergeSort(arr):
    if len(arr) < 2:
        return

    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]

    mergeSort(L)
    mergeSort(R)
    merge_two_sorted_lists(L, R, arr)


def merge_two_sorted_lists(a, b, arr):

    i = j = k = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1
        

arr = [12, 11, 13, 5, 6, 7]
mergeSort(arr)
print("Sorted array is:")
print(arr)


# Time Complexity: Merge Sort is  θ(nLogn) in all 3 cases (worst, average and best) as merge sort always 
# divides the array into two halves and takes linear time to merge two halves.
# Auxiliary Space: O(n)
# Algorithmic Paradigm: Divide and Conquer
# Sorting In Place: No in a typical implementation
# Stable: Yes
