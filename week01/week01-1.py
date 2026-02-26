class Solution:
    def numSteps(self, s: str) -> int:
        ans=0#羆ǐ碭˙
        n=int(s,2)#р﹃ノ秈俱计跑Θn
        while n>1:#ヘ夹:n程穦跑Θ1
            if n%2==0: n=n//2#案计
            else: n=n+1#计+1
            ans+=1
        return ans#羆璶ǐ碭˙
