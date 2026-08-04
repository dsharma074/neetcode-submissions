class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sdict = {}
        tdict = {}
        for i in range(len(s)):
            sdict[s[i]] = sdict.get(s[i],0) + 1
            tdict[t[i]] = tdict.get(t[i],0) + 1
        for i in sdict.keys():
            if sdict[i] != tdict.get(i,0): return False
        return True

        