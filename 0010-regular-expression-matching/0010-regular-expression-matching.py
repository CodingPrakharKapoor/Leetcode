class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s=" "+s
        p=" "+p
        dp=[[0]*len(p) for i in range(len(s))]
        dp[0][0]=1
        
        for i in range(1,len(p)):
            if(p[i]=='*'):
                dp[0][i]=dp[0][i-2]
        
        for i in range(1,len(s)):
            for j in range(1,len(p)):
                if(p[j] in {s[i],'.'}):
                    dp[i][j]=dp[i-1][j-1]
                elif(p[j]=='*'):
                    dp[i][j]=dp[i][j-2] or int(dp[i-1][j] and p[j-1] in {s[i],'.'})

        return bool(dp[-1][-1])