class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ######## Extension of two sum ###########
        nums.sort()
        lst = []
        seen = set()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            ndict = set()
            for j in range(i+1,len(nums)):
                if -nums[j]-nums[i] in ndict:
                    triplet = (nums[i],-nums[j]-nums[i], nums[j])
                    if triplet not in seen:
                        seen.add(triplet)
                        lst.append(list(triplet))
                ndict.add(nums[j])
        # print(lst)
        return lst