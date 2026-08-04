class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numset = dict()
        for i,val in enumerate(numbers):
            if target-val in numset:
                return [numset[target-val]+1,i+1]
            numset[val] = i
        