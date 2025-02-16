def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

my_list = [3,5,3,6,7,1,2,3,9,10,11,23,432,54,53,231,4,54,753,31,2343,5,64,34321,54,546,7,43,23,3443,673,6,1414,235,5]
print(selection_sort(my_list))

