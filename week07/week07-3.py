#week07-3.py
class Solution:
    def removeStars(self, s: str) -> str:
        ans=[]
        for c in s:
            if c=='*':ans.pop() #遇到星號,吐掉1個字母
            else: ans.append(c) #把不是星號的字母塞進去
        return ''.join(ans)  #用單單.join()把陣列join進去
