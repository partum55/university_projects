# Sorting Algorithms Implementation

def bubble_sort(arr):
    """
    Bubble Sort implementation - O(n^2)
    Repeatedly steps through the list, compares adjacent elements and swaps them if they are in wrong order.
    """
    # Create a copy to avoid modifying the original
    arr_copy = arr.copy()
    n = len(arr_copy)
    
    for i in range(n):
        # Flag to optimize if no swaps occur
        swapped = False
        for j in range(0, n-i-1):
            if arr_copy[j] > arr_copy[j+1]:
                arr_copy[j], arr_copy[j+1] = arr_copy[j+1], arr_copy[j]
                swapped = True
        # If no swapping occurred in this pass, array is sorted
        if not swapped:
            break
    return arr_copy


def selection_sort(arr):
    """
    Selection Sort implementation - O(n^2)
    Finds the minimum element from unsorted part and puts it at the beginning.
    """
    # Create a copy to avoid modifying the original
    arr_copy = arr.copy()
    n = len(arr_copy)
    
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
    return arr_copy


def insertion_sort(arr):
    """
    Insertion Sort implementation - O(n^2)
    Builds the sorted array one item at a time.
    """
    # Create a copy to avoid modifying the original
    arr_copy = arr.copy()
    
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        # Move elements greater than key to one position ahead
        while j >= 0 and arr_copy[j] > key:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = key
    return arr_copy


def merge_sort(arr):
    """
    Merge Sort implementation - O(n log n)
    Divide and conquer algorithm that divides array into two halves, sorts them and merges.
    """
    # Create a copy to avoid modifying the original
    arr_copy = arr.copy()
    
    if len(arr_copy) <= 1:
        return arr_copy

    # Divide array into two halves
    mid = len(arr_copy) // 2
    left = arr_copy[:mid]
    right = arr_copy[mid:]

    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    """Helper function for merge sort."""
    result = []
    i = j = 0

    # Merge the two sorted arrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    """
    Quick Sort implementation - O(n log n) average case, O(n^2) worst case
    Divide and conquer algorithm that picks a pivot and partitions array around it.
    """
    # Create a copy to avoid modifying the original
    arr_copy = arr.copy()
    
    if len(arr_copy) <= 1:
        return arr_copy

    # Helper function for partitioning
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    # Helper function for quick sort recursive implementation
    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)

    quick_sort_helper(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy


def heap_sort(arr):
    """
    Heap Sort implementation - O(n log n)
    Sorts by building a max heap and repeatedly extracting the maximum element.
    """
    # Create a copy to avoid modifying the original
    arr_copy = arr.copy()
    
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Check if left child exists and is greater than root
        if left < n and arr[largest] < arr[left]:
            largest = left

        # Check if right child exists and is greater than root
        if right < n and arr[largest] < arr[right]:
            largest = right

        # Change root if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr_copy)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr_copy, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr_copy[0], arr_copy[i] = arr_copy[i], arr_copy[0]
        heapify(arr_copy, i, 0)

    return arr_copy


def counting_sort(arr):
    """
    Counting Sort implementation - O(n+k) where k is the range of the input
    Works well for small ranges of positive integers.
    """
    if not arr:
        return []
    
    # Create a copy to avoid modifying the original
    arr_copy = arr.copy()
    
    # Find the maximum element in the input array
    max_element = max(arr_copy)
    min_element = min(arr_copy)
    range_of_elements = max_element - min_element + 1
    
    # Create a count array to store count of individual elements
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr_copy))]
    
    # Store count of each element
    for i in range(len(arr_copy)):
        count_arr[arr_copy[i] - min_element] += 1
    
    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    
    # Build the output array
    for i in range(len(arr_copy) - 1, -1, -1):
        output_arr[count_arr[arr_copy[i] - min_element] - 1] = arr_copy[i]
        count_arr[arr_copy[i] - min_element] -= 1
    
    return output_arr


def radix_sort(arr):
    """
    Radix Sort implementation - O(d*(n+k)) where d is number of digits and k is the range
    Works well for integers by sorting them digit by digit.
    """
    if not arr:
        return []
    
    # Create a copy to avoid modifying the original
    arr_copy = arr.copy()
    
    # Find the maximum number to know number of digits
    max_num = max(arr_copy)
    
    # Do counting sort for every digit
    exp = 1
    while max_num // exp > 0:
        # Count sort for current digit
        n = len(arr_copy)
        output = [0] * n
        count = [0] * 10
        
        # Store count of occurrences
        for i in range(n):
            index = arr_copy[i] // exp
            count[index % 10] += 1
            
        # Change count[i] so that count[i] contains actual position of this digit
        for i in range(1, 10):
            count[i] += count[i - 1]
            
        # Build the output array
        for i in range(n - 1, -1, -1):
            index = arr_copy[i] // exp
            output[count[index % 10] - 1] = arr_copy[i]
            count[index % 10] -= 1
            
        # Copy the output array to arr_copy
        for i in range(n):
            arr_copy[i] = output[i]
            
        # Move to next digit
        exp *= 10
        
    return arr_copy


def shell_sort(arr):
    """
    Shell Sort implementation - Between O(n) and O(n^2)
    Modification of insertion sort that allows exchange of far elements.
    """
    # Create a copy to avoid modifying the original
    arr_copy = arr.copy()
    n = len(arr_copy)
    
    # Start with a big gap, then reduce the gap
    gap = n // 2
    
    while gap > 0:
        # Do a gapped insertion sort
        for i in range(gap, n):
            # Save arr_copy[i] in temp and make a hole at position i
            temp = arr_copy[i]
            
            # Shift earlier gap-sorted elements up until the correct location for arr_copy[i] is found
            j = i
            while j >= gap and arr_copy[j - gap] > temp:
                arr_copy[j] = arr_copy[j - gap]
                j -= gap
                
            # Put temp in its correct location
            arr_copy[j] = temp
            
        # Reduce the gap
        gap //= 2
        
    return arr_copy
