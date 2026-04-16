#week08-5.py
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #笨方法:for迴圈
        N=len(nums) #陣列大小N
        if N==1:return 0 #i=0最大

        for i in range(N): 每個index i都去嘗試左邊
            if i==0:  #沒有左邊,只測右邊
                if nums[i]>nums[i+1]:return i
            elif i==N-1: #最右邊,沒有右邊,只測左邊
                if nums[i]>nums[i-1]:return i
            elif nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
