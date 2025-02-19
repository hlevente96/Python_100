def hourglassSum(arr):
    max_ = float('-inf')
    for i in range(4):
        for j in range(4):
            new_max = sum(arr[i][j:j+3])+sum(arr[i+2][j:j+3])+arr[i+1][j+1]
            if new_max > max_:
                max_ = new_max
    return max_

arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]
print(hourglassSum(arr))