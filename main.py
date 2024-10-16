from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_dict = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in num_dict:
            return [num_dict[complement], i]

        num_dict[num] = i
        
    return []

# Test cases

nums = [2, 7, 11, 15]
target = 9
print(f"Input: nums = {nums}, target = {target}")
print(f"Output: {twoSum(nums, target)}")

nums = [3, 2, 4]
target = 6
print(f"Input: nums = {nums}, target = {target}")
print(f"Output: {twoSum(nums, target)}")

nums = [3, 3]
target = 6
print(f"Input: nums = {nums}, target = {target}")
print(f"Output: {twoSum(nums, target)}")