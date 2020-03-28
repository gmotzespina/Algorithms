import timeit

test1 = """
def is_num_in_list(nums: [int], num_to_search: int) -> bool:

    for num in nums:
        if num == num_to_search:
            return True

    return False

list1 = range(159) 

is_num_in_list(list1, 158)
"""
elapsed_time1 = timeit.timeit(test1, number=100)/100
print(elapsed_time1)

test2 = """
def is_num_in_list_python_way(nums: [int], num_to_search: int) -> bool:

    return num_to_search in nums

list1 = range(159) 
is_num_in_list_python_way(list1, 158)
"""

elapsed_time2 = timeit.timeit(test2, number=100)/100

print(elapsed_time2)
