class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        ans=""
        for i in range(num):
            if(sum>9):
                sum-=9
                ans+="9"
            else:
                ans+=str(sum)
                sum=0
                break
        
        if(sum>0):
            # print(ans)
            return ""
        return ans+"0"*(num-len(ans))