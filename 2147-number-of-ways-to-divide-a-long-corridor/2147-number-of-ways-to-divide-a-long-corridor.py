class Solution:
    def numberOfWays(self, corridor: str) -> int:
        count=corridor.count('S')
        if(count<2 or count%2!=0):return 0
        ans=1
        seen=0
        p=0
        for i in corridor:
            if(i=='S'):
                seen+=1
                if(seen>2 and seen%2==1):
                    ans=ans*(p+1)
                    p=0
            elif(seen%2==0 and seen>0):
                p+=1
        return ans%int(1e9+7)