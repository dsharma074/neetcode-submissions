class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= [i.lower() for i in s if i.isalnum()]
        if not s:
            return True
        for i in range(len(s)//2+1):
            if s[i] != s[len(s)-1-i]:
                print(s[i],s[len(s)-1-i])
                return False
        return True
