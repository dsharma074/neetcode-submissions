class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        chardict = dict()
        # chardict[s[l]] = l 
        max_len = 0
        while l<=r<= len(s)-1:
            if s[r] in chardict:
                term = chardict[s[r]]
                while l < term+1:
                    chardict.pop(s[l])
                    l +=1
            chardict[s[r]] = r
            print(l,r)
            max_len = max(max_len, r-l+1)
            r +=1
        return max_len



