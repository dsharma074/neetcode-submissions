class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def key_map(lst):
            key = [0]*26
            for i in lst:
                rank = (ord(i)-ord("a"))
                key[rank] += 1
            return tuple(key)
        dicti = defaultdict(list)
        for l in strs:
            key = key_map(l)
            dicti[key].append(l)
        return list(dicti.values())
        