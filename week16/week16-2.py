class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        #i:瞷刚计,k临璶碭计,n:临璶干ぶ
        def helper(now,i,k,n):
            if k==0 and n==0:
                ans.append(now)
                return
            if k<0 or n<0:return
            for ii in range(i,10): #i....9ぇ丁计
                #瞷狦ii
                helper(now+[ii],ii+1,k-1,n-ii)
                #Ω璶代刚ii+1,ノ奔1计,羆㎝ぶii
        helper([],1,k,n)
        return ans
