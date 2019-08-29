
def binary_search(arr, target, low=None, high=None):
    if low == None:
        low = 0

    if high == None:
        high = len(arr)

    if not arr or low >= high:
        return -1

    mid_index = ((high - low) // 2) + low

    if target == arr[mid_index]:
        return mid_index
    elif target < arr[mid_index]:
        return binary_search(arr, target, low, mid_index)
    elif target > arr[mid_index]:
        return binary_search(arr, target, mid_index + 1, high)

    return -1


def find_rotation_index(arr, low=None, high=None):
    if low == None:
        low = 0

    if high == None:
        high = len(arr)

    if not arr or low >= high:
        return -1

    mid_index = ((high - low) // 2) + low

    if mid_index + 1 < len(arr) and arr[mid_index + 1] < arr[mid_index]:
        return mid_index
    elif arr[low] < arr[mid_index]:
        return find_rotation_index(arr, mid_index + 1, high)
    elif arr[low] > arr[mid_index]:
        return find_rotation_index(arr, low, mid_index)

    return -1
