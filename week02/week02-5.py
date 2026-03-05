#week02-5.py
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()#小到大排好,等一下左邊挑一個,右邊挑一個
        ans=0
        i,j=0,len(nums)-1#最左邊i對應最小
        while i<j:#還沒有撞再一起,就可以左右個挑一個
            if nums[i]+nums[j]==k:
                ans+=1
                i,j=i+1,j-1
            if nums[i]+nums[j]<k:
                i=i+1
            if nums[i]+nums[j]>k:
                j=j-1
        return ans
