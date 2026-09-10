class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        mincost = {}
        mincost[0] = 0
        mincost[1] = 0
        
        def costcalculate(num):
            if num in mincost:
                return mincost[num]
            else:
                mincost[num] = min(cost[num-1]+costcalculate(num-1), cost[num-2]+ costcalculate(num-2))
                return mincost[num]
        
        return costcalculate(n)

        