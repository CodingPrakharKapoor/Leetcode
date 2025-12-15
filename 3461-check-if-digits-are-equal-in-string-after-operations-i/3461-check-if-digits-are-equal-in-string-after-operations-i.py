class Solution:
    def hasSameDigits(self, s: str) -> bool:
        def func(n):
            ans=""
            lst=[int(x) for x in n]
            for i in range(1,len(n)):
                x=(lst[i-1]+lst[i])%10
                ans+=str(x)
            return str(ans)
        while(len(s)>2):
            s=func(s)
            print(s)
        return s[0]==s[-1]