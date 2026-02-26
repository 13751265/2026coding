#week01-4.py
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]#答案的True和False將塞在裡面
        best=max(candies)#目前小朋友最多有幾顆糖
        for candie in candies:#逐一檢查,把extracandies給小朋友
            if candie + extraCandies >=best: ans.append(True)
            else: ans.append(False)#他會不會>=最多的,依序塞入ans
        return ans
