class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_count = 0
        for i in numset:
            if i-1 not in numset:###beginning of the string
                count = 0
                while i in numset:
                    count+=1
                    i +=1
                max_count = max(max_count,count)
        return max_count