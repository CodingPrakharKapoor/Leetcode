class Solution:
    def largestEven(self, s: str) -> str:
        lst=[]
        for i in range(len(s)):
            if(s[i]=="2"):
                lst.append(i)
        if(not lst):
            return ""
        return s[:lst[-1]+1]