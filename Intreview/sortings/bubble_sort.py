import time

def bubble_sort(list_to_sort):
    list_length = len(list_to_sort)
    for i in range(list_length):
        sort_happened = False
        for j in range(list_length-i-1):
            if list_to_sort[j] > list_to_sort[j+1]:
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
                sort_happened = True
        if not sort_happened:
            break
    return list_to_sort

my_list = [3,5,3,6,7,1,2,3,9,10,11,23,432,54,53,231,4,54,753,31,2343,5,64,34321,54,546,7,43,23,3443,673,6,1414,235,5]

start = time.time()
for i in range(10000):
    bubble_sort(my_list)
end = time.time()
print(end-start)
print(bubble_sort(my_list))


