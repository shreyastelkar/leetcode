# 3396. Minimum Number of Operations to Make Elements in Array Distinct
def minimumOperations(nums: List[int]) -> int:
    num_ops = 0
    l = 0
    numbers = copy.copy(nums)
        
    while l < len(numbers) and len(list(set(numbers[l:]))) != len(numbers[l:]):
        # while the sublist is not the same as the set of the sublist, 
        # indicating duplicates
        if len(numbers[l:]) < 3:
            num_ops += 1
            break
        else:            
            num_ops += 1
            l += 3

    return num_ops

print(minimumOperations([1,2,3,4,2,3,3,5,7]))
