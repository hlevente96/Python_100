def brute_sliding(k, lst):
    total = 0
    for i in range(len(lst)-k+1):
        total = max(total, sum(lst[i:i+k]))
    return total

def sliding(k,lst):
    total = sum(lst[:k])
    max_ = total
    for i in range(len(lst)-k):
        total = total - lst[i] + lst[i+k]
        max_ = max(total,max_)
    return max_

def moving_average(k, lst):
    averages = []
    curr = sum(lst[:k])
    averages.append(curr/k)
    for i in range(len(lst)-k):
        curr = curr - lst[i] + lst[i+k]
        averages.append(curr/k)
    return averages


test_lst = [1,3,5,3,7,5,9,3,2,1,6,7,5,4,8,8,7,3,4,5,9,8,9,2,1,1,5,6,7,5,9,9,9,9,9]
print(brute_sliding(5,test_lst))
print(sliding(5, test_lst))
print(moving_average(5, test_lst))