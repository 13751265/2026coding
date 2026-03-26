#week05-6.py
#橫的,直的 有幾組全相同
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter=Counter() #Hash Map可以知道有哪些row出現幾次
        for row in grid:
            counter[tuple(row)]+=1
            #tuple()可以把陣列[3,1,2,2],變不會動(3,1,2,3)

        ans=0 #有幾組
        for col in zip(*grid): #矩陣transpose再取出col
            ans+=counter[tuple(col)]
        return ans
