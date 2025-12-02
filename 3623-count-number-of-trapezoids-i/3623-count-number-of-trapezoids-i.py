class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        freq=defaultdict(int)
        for i in range(len(points)):
            x=points[i][0]
            y=points[i][1]
            freq[y]+=1
        lst=[]
        for y in freq:
            n=freq[y]
            lst.append((n*(n-1)//2))
        if(not lst):
            return 0
        s=lst[0]
        ans=0
        for i in range(1,len(lst)):
            ans+=s*lst[i]
            s+=lst[i]
        return ans%int(1e9+7)