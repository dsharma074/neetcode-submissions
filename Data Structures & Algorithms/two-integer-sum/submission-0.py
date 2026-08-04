class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numset = {}
        for i, val in enumerate(nums):
            if target-val in numset:
                return [numset[target-val],i]
            numset[val] = i        