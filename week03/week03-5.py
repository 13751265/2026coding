#week03-5
#陣列裡,一定要刪掉一個,問剩下的陣列裡,最長的1有幾個
#sliding window伸縮自如的蛇
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N=len(nums)#陣列的長度
        zeros=0 #蛇體內有幾個0
        tail=0 #蛇的尾巴一開始停在0的地方
        ans=0 #蛇最長的長度
        for head in range(N): #蛇的頭,逐一往右吃
            if nums[head]==0:zeros+=1 #如果吃到有毒的0,zeros+1
            while zeros > 1: #有毒的0太多了
                if nums[tail]==0:zeros-=1 #拉出有毒的0,zeros-1
                tail+=1 #尾巴吐之後.右移
            ans=max(ans,head-tail+1)#更新蛇的最大長度
        return ans-1
