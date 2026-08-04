class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicti = defaultdict(int)
        for i in nums:
            dicti[i] +=1
        val = list(dicti.keys())
        val.sort(key = lambda x: dicti[x])
        return val[-k:]


        