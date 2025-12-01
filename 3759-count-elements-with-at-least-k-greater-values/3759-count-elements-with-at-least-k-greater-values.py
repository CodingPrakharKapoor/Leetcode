class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        s=list(set(nums))
        freq=Counter(nums)
        s.sort()
        print(s)
        pref=[]
        for i in s[::-1]:
            if(not pref):pref.append(freq[i])
            else:pref.append(pref[-1]+freq[i])
        pref=pref[::-1]
        print(pref)
        ans=0
        for i,val in enumerate(s):
            if(pref[i]-freq[val]>=k):
                ans+=freq[val]
        return ans