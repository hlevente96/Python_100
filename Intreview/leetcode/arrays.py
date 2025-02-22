############ FIRST ############
def remove_duplicates(nums):
    if not nums:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1
    return k

def remove_duplicate_2(nums):
    return len(set(nums))

test = [1,1,1,2,2,3,3,4,4,4,5,5,5,6,6,7,7,7,7,7]
print(remove_duplicates(test))
print(remove_duplicate_2(test))

############ SECOND ############
def max_profit(prices):
    if not prices:
        return 0
    profit = 0
    for i in range(len(prices)-1):
        if prices[i] < prices[i+1]:
            profit += prices[i+1]-prices[i]
    return profit

def max_profit_2(prices):
    if not prices:
        return 0
    profit, holding, buy = 0, False, 0
    for i in range(len(prices)-1):
        if not holding and prices[i] < prices[i+1]:
            buy = prices[i]
            holding = True
        elif holding and prices[i] > prices[i+1]:
            profit += prices[i] - buy
            holding = False
    if holding:
        profit += prices[-1] - buy
    return profit

print(f"Profit: {max_profit_2([1, 4, 2, 1, 3, 5, 8, 1, 5, 9])}")

############ THIRD ############
def rotate_array(arr,k):
    n = len(arr)
    k = k%n
    arr[:] = arr[-k:] + arr[:-k]
    print(arr)

rotate_array([1,2,3,4,5,6,7,8],5)

############ FOURTH ############
def contains_duplicate(nums):
    elements = set()
    for i in range(len(nums)):
        if nums[i] in elements:
            return True
        else:
            elements.add(nums[i])
    return False

def contains_duplicate_2(nums):
    return len(set(nums)) != len(nums)

print(contains_duplicate([1,2,3,4,5,6,7,8,9,9]))
print(contains_duplicate_2([1,2,3,4,5,6,7,8,9,9]))

############ FIFTH ############
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

nums = [3, 3, 4, 1, 2, 1, 2, 5, 6, 4, 6]
print(single_number(nums))
