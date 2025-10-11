class Solution:
    def maximumTotalDamage(self, powers: List[int]) -> int:
        freq=defaultdict(int)
        for power in powers:
            freq[power]+=1

        up=list(freq.keys())
        up.sort()

        uc=len(up)
        if(uc==1):
            return up[0]*freq[up[0]]

        maxDamage=[0]*(uc+1)
        for i in range(1,uc+1):
            curr=up[i-1]*freq[up[i-1]]
            take=curr

            for j in range(i-2,-1,-1):
                if(up[i-1]-up[j]>2):
                    take+=maxDamage[j+1]
                    break

            dont=maxDamage[i - 1]
            maxDamage[i]=max(take, dont)

        return maxDamage[uc]

