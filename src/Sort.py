
def merge_sort(arr):
    if not arr or len(arr) == 1:
        return arr

    return merge(merge_sort(arr[:len(arr) // 2]), merge_sort(arr[len(arr) // 2:]))

def merge(arr1, arr2):
    if not arr1 and not arr2:
        return []

    if not arr1:
        return arr2

    if not arr2:
        return arr1

    result_arr = [None] * (len(arr1) + len(arr2))
    result_idx = 0
    arr1_idx = 0
    arr2_idx = 0

    while result_idx < len(result_arr):

        # copy the rest of arr2
        if arr1_idx == len(arr1):
            result_arr[result_idx] = arr2[arr2_idx]
            arr2_idx += 1

        # copy the rest of arr1
        elif arr2_idx == len(arr2):
            result_arr[result_idx] = arr1[arr1_idx]
            arr1_idx += 1

        elif arr1[arr1_idx] < arr2[arr2_idx]:
            result_arr[result_idx] = arr1[arr1_idx]
            arr1_idx += 1

        else:
            result_arr[result_idx] = arr2[arr2_idx]
            arr2_idx += 1

        result_idx += 1

    return result_arr


def quick_sort(arr):
    if not arr or len(arr) == 1:
        return arr

    return quick_sort_helper(arr, 0, len(arr) - 1)

def quick_sort_helper(arr, start, end):
    if (start >= end):
        return arr

    pivot_element = arr[ (start + end) // 2]
    i = partition(arr, start, end, pivot_element)

    quick_sort_helper(arr, start, i - 1)
    quick_sort_helper(arr, i, end)

    return arr

def partition(arr, i, j, pivot_element):
    while i <= j:
        while arr[i] < pivot_element:
            i += 1

        while arr[j] > pivot_element:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    return i

