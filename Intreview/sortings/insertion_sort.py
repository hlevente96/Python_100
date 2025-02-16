def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        element = arr[i]
        j = i-1
        while j >= 0 and arr[j] > element:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = element
    return arr

my_list = [3,5,3,6,7,1,2,3,9,10,11,23,432,54,53,231,4,54,753,31,2343,5,64,34321,54,546,7,43,23,3443,673,6,1414,235,5]
print(insertion_sort(my_list))