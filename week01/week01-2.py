#week01-2
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""#答案在ans
        N1,N2=len(word1),len(word2)
        i,j=0,0#word1[i] v.s. word2[j]
        while i<N1 or j<N2:#只要任一個有剩下
            if i<N1:ans+=word1[i]#沒用完
            if j<N2:ans+=word2[j]#沒用完
            i,j=i+1,j+1#都換下一位
        return ans#答案在這裡
