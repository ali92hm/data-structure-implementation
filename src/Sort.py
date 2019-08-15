
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


def quick_sort(arr, start=None, end=None):
    if not arr or len(arr) == 1:
        return arr

    if not start:
        start = 0

    if not end:
        end = len(arr) - 1

    if start >= end:
        return

    pivot_element = arr[ (start + end) // 2]
    i = start
    j = end

    while i < j:
        if arr[i] < pivot_element:
            i += 1

        elif arr[j] > pivot_element:
            j -= 1

        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    quick_sort(arr, start, i)
    quick_sort(arr, i + 1, end)

    return arr
