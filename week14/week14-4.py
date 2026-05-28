#week14-4
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache #遇到dp的題目,就用TOP-DOWN DP
        def helper(i): #如果搶到第i個房間,最後可以拿到多少錢
            if i>=len(nums):return 0 #整條街走完了,沒得搶了
            return nums[i]+max(helper(i+2),helper(i+3))
            #函式呼叫函式,來解TOP-DOWN DP
        return max(helper(0),helper(1))
