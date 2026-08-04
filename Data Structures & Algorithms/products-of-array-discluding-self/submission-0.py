class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_array = len(nums)
        left = [1]*len_array
        right = [1]*len_array
        for i in range(1,len(nums)):
            left[i] = nums[i-1]*left[i-1]
            right[len_array - 1 - i] = nums[len_array - i]*right[len_array - i]
        for i in range(len(left)):
            left[i] = left[i]*right[i]
        return left


        