# 242. Valid Anagram
def isAnagram(self, s: str, t: str) -> bool:
    def _calculate_letter_count(word: str) -> dict[str, int]:
        hm_freq = {}
        for letter in word:
            hm_freq[letter] = hm_freq.get(letter, 0) + 1
        return hm_freq

    if _calculate_letter_count(s) == _calculate_letter_count(t):
        result = True
    else:
        result = False

    return result

# 1. Two Sum
def twoSum(self, nums: List[int], target: int) -> List[int]:
    hm = {}
    res = None
    for i in range(len(nums)):
        if target - nums[i] in hm:
            res = [hm[target - nums[i]], i]
            break
        else:
            hm[nums[i]] = i
    return res

# 217. Contains Duplicates
def containsDuplicate(self, nums: List[int]) -> bool:
    seen = set()
    result = False
    for num in nums:
        if num not in seen:
            seen.add(num)
        else:
            result = True
            break                
        return result

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

