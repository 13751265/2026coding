#week04-3.py
#找到陣列nums裡只出現過一次的偶數,第一次出現的位置
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        ans=-1 #找不到答案,會是-1
        N=len(nums)#有N個數
        H=[0]*200
        for i in range(N):#第一次處理
            H[nums[i]]+=1 #把出現的數字塞進H[]裡
        for i in range(N):#逐一檢查
            if nums[i]%2==0 and H[nums[i]]==1: #偶數才處理
                return nums[i] #找出答案
        return -1
