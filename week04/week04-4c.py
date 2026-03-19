#week04-4c.py(重寫week04-4b.py)
#找到陣列nums裡只出現過一次的偶數,第一次出現的位置
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        H=Counter(nums) #使用進階資料結構,可以統計數量
        for nn in nums: #再來一次,逐一取出來
            if nn%2==0 and H[nn]==1: #偶數and落單
                return nn
        return -1
