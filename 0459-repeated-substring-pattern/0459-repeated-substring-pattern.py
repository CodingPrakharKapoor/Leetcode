class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        st=""
        for i in range(0,len(s)//2):
            st+=s[i]
            if(s.count(st)*len(st)==len(s)):
                return True
        return False