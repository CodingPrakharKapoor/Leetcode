class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s=sum(nums)
        rem=s%p
        if(rem==0):return 0
        pref=0
        mini=len(nums)
        dic={0:-1}
        for i,num in enumerate(nums):
            pref+=num
            t=(pref%p-rem)%p
            if(t in dic):
                mini=min(mini,i-dic[t])
            dic[pref%p]=i
        if(mini==len(nums)):
            return -1
        return mini