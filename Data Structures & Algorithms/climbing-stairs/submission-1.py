class Solution:
    def climbStairs(self, n: int) -> int:
        dicti = {}
        dicti[1] = 1
        dicti[2] = 2
        def uniquevalues(n):
            if n in dicti:
                return dicti[n]
            dicti[n] = uniquevalues(n-2)+uniquevalues(n-1)
            return dicti[n]
        return uniquevalues(n)
        