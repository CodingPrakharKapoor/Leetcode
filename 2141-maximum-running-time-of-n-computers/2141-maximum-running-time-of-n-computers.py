class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        if(len(batteries)==n):return min(batteries)
        batteries.sort()
        s=sum(batteries[:-n])
        batteries=batteries[-n:]

        for i in range(len(batteries)-1):
            d=batteries[i+1]-batteries[i]
            need=d*(i+1)
            if(need>s):
                x=s//(i+1)
                for j in range(i+1):
                    batteries[j]+=x
                    s-=x
                break
            s-=need
            for j in range(i+1):
                batteries[j]=batteries[i+1]

        d=s//len(batteries)
        m=s%len(batteries)
        for i in range(len(batteries)):
            batteries[i]+=d
        batteries[-1]+=m
        return min(batteries)