#week03-4,py
#你可以把k個0翻轉成1,在這之後有幾個1
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros=0 #一開始的蛇,度自裡沒有0
        N=len(nums)#陣列長度
        ans=0
        tail=0#尾巴一開始在0的位置
        for head in range(N): #蛇頭,慢慢往右吃
            if nums[head]==0: #吃到一個0
                zeros +=1 #體內0增加
                #if zeros>k: #超過身體可以容納的上限
                while zeros>k:#要用while迴圈重複排出
                    if nums[tail]==0: #吐掉多餘的0
                        zeros-=1
                    tail+=1 #尾巴移動
            ans=max(ans,head-tail+1)#更新答案
        return ans#最長的
