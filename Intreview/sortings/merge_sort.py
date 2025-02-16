def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # Divide
    middle = len(arr) // 2
    left_side = merge_sort(arr[:middle])
    right_side = merge_sort(arr[middle:])
    #Merging
    return merge(left_side, right_side)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

array = [8,4,3,5,6,1,9,2]
print(merge_sort(array))

