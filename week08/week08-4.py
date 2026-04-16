#week08-4.py
#想知道某種spells[i]魔法,配幾種藥水可以成功
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort() #藥水小到大排好
        p=len(potions)
        ans=[]
        for spell in spells: #每一種魔法,都嘗試一次
            now=p-bisect_left(potions,success/spell)
            ans.append(now)
        return ans
