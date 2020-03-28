def multipliers(nums: [int], multiplies_to: int) -> [int]:

    seen = {}

    for num in nums:

        if multiplies_to%num == 0:
            complement = multiplies_to//num
            if num not in seen:
                seen[complement] = num
            else:
                return [num, seen[num]]

    return [] 

nums = multipliers([1, 2, 3, 11, -5, 4], 20)
print(nums)
