class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        freq=Counter(nums)
        lst=sorted(list(freq))
        ans=[]
        while(len(ans)<len(nums)):
            for i in lst:
                if(freq[i]>=1):ans.append(i)
                freq[i]-=1
        return ans