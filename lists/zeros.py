
def move_zeros_back_changing_order(nums: [int]) -> [int]:

    nums.sort()
    nums.reverse()

    return nums

def move_zeros_back(nums: [int]) -> [int]:

    zeros_found = []

    for index, num in enumerate(nums):
        if num == 0:
            zeros_found.append(index)
        else:
            zeros_found_length = len(zeros_found)
            if zeros_found_length > 0:
                nums[zeros_found[0]] = num
                nums[index] = 0 
                del zeros_found[0]

    return nums

nums = [1, 2, 0, 0, 4, 3, 0];

print(nums)

print(move_zeros_back_changing_order(nums[:]))

print(move_zeros_back(nums))
nums = [0,3,1,0,2,5,0,0];
print(move_zeros_back(nums))
