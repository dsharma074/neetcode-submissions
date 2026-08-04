class Solution:
    def trap(self, height: List[int]) -> int:
        maxl = [0]*len(height)
        maxr = [0]*len(height)
        hlength = len(height)-1
        for i in range(hlength+1):
            if i == 0:
                maxl[i]=height[i]
                maxr[hlength] = height[hlength]
            else:
                maxl[i] = max(height[i],maxl[i-1])
                maxr[hlength - i] = max(height[hlength-i], maxr[hlength-i+1])
        totalwater = 0
        for i in range(hlength +1):
            water = min(maxl[i], maxr[i]) -height[i]
            totalwater += water
        print(maxl)
        print(maxr)
        return totalwater


        
        