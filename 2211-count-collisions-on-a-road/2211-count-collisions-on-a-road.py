class Solution:
    def countCollisions(self, s: str) -> int:
        n=len(s)
        left=0
        right=n-1
        while(left<n and s[left]=="L"):
            left+=1
        while(right>=0 and s[right]=="R"):
            right-=1
        ans=0
        for i in range(left,right+1):
            if(s[i]!="S"):
                ans+=1
        return ans