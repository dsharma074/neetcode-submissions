class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not set(t).issubset(set(s)):
            return ""
        sdict = {}
        tdict = {}
        for k in s:
            sdict[k] = sdict.get(k,0)+1
        for k in t:
            tdict[k] = tdict.get(k,0)+1
        # for key in tdict:
        #     if tdict[key]>sdict[key]:
        #         return ""
        
        left = 0

        bestleft = 0
        bestright = float("inf")

        required = len(tdict)
        formed = 0
        window = {}

        for right in range(len(s)):
            window[s[right]] = window.get(s[right],0)+1
            if s[right] in tdict:
                if window[s[right]] == tdict[s[right]]:
                    formed += 1
            while formed == required:
                if bestright-bestleft+1 > right-left+1:
                    bestright = right
                    bestleft = left
                
                window[s[left]] -= 1
                if s[left] in tdict:
                    if window[s[left]] < tdict[s[left]]:
                        formed -=1
                left += 1
            # print(s[left],s[right], s[bestleft])
        if bestright == float("inf"):
            return ""
        return s[bestleft:bestright+1]





