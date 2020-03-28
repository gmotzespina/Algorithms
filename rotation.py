
def is_rotation(l1: [int], l2: [int]) -> bool:

    seen_nums = []
    first_num = l1[0]  
    index = 0
    if len(l1) != len(l2):
        return False

    if first_num not in l2:
        return False

    index = l2.index(first_num)
    for num in l1:
        if index < len(l2):
            if num != l2[index]:
                return False
        else: 
            index = 0
        index += 1
    return True

l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [7,8,9,10,1,2,3,4,5,8]
print(is_rotation(l1, l2))
