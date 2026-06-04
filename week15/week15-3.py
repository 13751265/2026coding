#week15-3
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def helper(i,hasStack):
            if i==len(prices):return 0 #終止條件
            #手上有股票,可以考慮要不要賣,賣的時候要付手續費
            if hasStack:ans=prices[i]+helper(i+1,False)-fee #得到錢prices[i]
            #手上沒有股票,可以考慮要不要買
            else:ans= -prices[i]+helper(i+1,True) #花了錢prices[i]得到股票
            #不賣,也不買
            return max(ans,helper(i+1,hasStack)) #狀態相同,直接換下一天

        return helper(0,False) #從第0天開始思考,手上沒有股票
