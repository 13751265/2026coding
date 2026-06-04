#week15-4
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M,N=len(word1),len(word2) #ㄢ﹃
        @cache
        def helper(i,j): #瞷璶矪瞶word1[i]vs.word2[j]
            if i==M and j==N:return 0 #常ǐ程
            if i==M:return N-j #word2逞,常璶奔
            if j==N:return M-i #word1逞,常璶奔
            if word1[i]==word2[j]:return helper(i+1,j+1)
            return min(helper(i+1,j),helper(i,j+1),helper(i+1,j+1))+1
        return helper(0,0)
