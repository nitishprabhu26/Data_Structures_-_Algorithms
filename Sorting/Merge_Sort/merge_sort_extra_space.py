# Merge Sort extra space (by creating a new array):

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]

    L = mergeSort(L)
    R = mergeSort(R)

    return merge_two_sorted_lists(L,R)

def merge_two_sorted_lists(a,b):
    sorted_list = []
    
    i=j=0
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1
    while i<len(a):
        sorted_list.append(a[i])
        i+=1

    while j<len(b):
        sorted_list.append(b[j])
        j+=1

    return sorted_list

arr = [12, 11, 13, 5, 6, 7]
sorted_final_array = mergeSort(arr)
print("Sorted array is:")
print(sorted_final_array)


# Time Complexity: Merge Sort is  θ(nLogn) in all 3 cases (worst, average and best) as merge sort always divides the array into two halves and takes linear time to merge two halves.
# Auxiliary Space: O(n)
# Algorithmic Paradigm: Divide and Conquer
# Sorting In Place: No in a typical implementation
# Stable: Yes
