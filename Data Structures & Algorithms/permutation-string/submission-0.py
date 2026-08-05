class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not set(s1).issubset(set(s2)):
            return False
        dsone = {}
        for i in s1:
            dsone[i] = dsone.get(i,0)+1

        i = 0
        j = 0
        while j < len(s2):
            if len(s1) != len(s2[i:j+1]):
                j += 1
                print(i,j)
                continue
            elif set(s2[i:j+1]).issubset(set(s1)):
                dsclone  = dsone.copy()
                for k in s2[i:j+1]:
                    dsclone[k] -= 1
                summ = 0
                print(dsclone)
                for key in dsclone.keys():
                    summ += dsclone[key]
                    if dsclone[key] != 0:
                        break
                if summ == 0:
                    return True
            i += 1
            print(i,j)
        return False


        