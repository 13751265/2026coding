#week02-3.py
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N1,N2=len(s),len(t)
        if N1==0:return True

        i=0
        for k in range(N2): #右邊一個個去試
            if s[i]==t[k]:#找到一個(左右)符合的了
                i+=1 #左邊的i往右邊升一級
            if i==N1:#左邊的i有走到左邊的結束
                return True
        #沒有走到最後
        return False
