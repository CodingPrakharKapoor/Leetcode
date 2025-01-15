class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=0
        stack=[]
        for i in s:
            if(i=="("):
                stack.append(i)
                maxi=max(maxi,len(stack))
            elif(i==")"):
                stack.pop()
        return maxi