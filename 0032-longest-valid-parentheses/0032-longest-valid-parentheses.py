class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lst=[-1]
        maxi=0

        for i,num in enumerate(s):
            if(num=="("):
                lst.append(i)
            else:
                lst.pop()
                if(not lst):
                    lst.append(i)
                else:
                    maxi=max(maxi,i-lst[-1])
        return maxi