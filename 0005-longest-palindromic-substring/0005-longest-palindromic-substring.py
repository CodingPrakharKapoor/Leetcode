class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(s==s[::-1]):return s
        st=""
        maxi=0
        for i in range(len(s)):
            s1=""
            for j in range(i,len(s)):
                s1+=s[j]
                if(s1==s1[::-1] and maxi<len(s1)):
                    maxi=max(maxi,len(s1))
                    st=s1
        return st
        