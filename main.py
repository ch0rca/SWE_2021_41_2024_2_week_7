from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:

    dictionary = {}

    for i, num in enumerate(nums):
        dictionary[num] = i

    for i, num in enumerate(nums):
        answer = target - num

        if answer in dictionary and dictionary[answer] != i:
            return [i, dictionary[answer]]
        
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