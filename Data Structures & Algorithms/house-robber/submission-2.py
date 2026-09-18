class Solution:
    def rob(self, nums: List[int]) -> int:
        numlen = len(nums)-1
        robmemo = {}
        robmemo[0] = nums[0]
        if numlen > 0:
            robmemo[1] = max(nums[0],nums[1])
        def robcost(n):
            if n in robmemo:
                return robmemo[n]
            else:
                robmemo[n] = max(nums[n]+ robcost(n-2), robcost(n-1))
                return robmemo[n]
        return robcost(numlen)
            

        