
# [1,2,5,0,6,15,1,1,7,0,6,0,0,15,5,1,0,0,2,1] target = 14
def max_subarray(nums, target): 
    
    max_length = [0,0]

    window = []
    total = 0
    left = 0
    right = 0
    while right < len(nums): # 1 < 11 -1 = 10
        if total+nums[right] <= target: # 1 <= 14, 3 <=14
            total += nums[right] # 1, 3
            window = [left, right] # [0, 0], [0, 1]
            right += 1 # 1
        else:
            if (window[1] - window[0]) > (max_length[1] - max_length[0]) and total == target:
                max_length[0] = window[0]
                max_length[1] = window[1]
            total -= nums[left]
            left += 1

        if left == right:
            right += 1
            left += 1
    if (window[1] - window[0]) > (max_length[1] - max_length[0]) and total == target:
        max_length[0] = window[0]
        max_length[1] = window[1]


    return max_length


print(max_subarray([1,2,5,0,15,1,1,7,15,5,1,0,0,2,1], 9))
