class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dicti = {}
        i = 0
        j = 0
        dicti[s[i]] = 1
        # dicti[s[j]] = dicti.get(s[j],0) + 1
        longlength = 0
        while j < len(s):
            summ = 0
            maxfreq = 0
            for key in dicti.keys():
                summ += dicti[key]
                maxfreq = max(maxfreq, dicti[key])

            if summ - maxfreq <= k:
                longlength = max(j-i+1, longlength)
                # print(i,j, summ, longlength)
                j +=1
                if j<len(s):
                    dicti[s[j]] = dicti.get(s[j],0)+1
            else:
                dicti[s[i]] -= 1
                i +=1

        return longlength





        