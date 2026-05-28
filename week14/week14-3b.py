#week14-b
#踩在第i格的梯子上,要付出cost[i]的代價,每次可跨1格or2格
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N=len(cost)
        a=[0]*(N+1)
        a[0]=cost[0]
        a[1]=cost[1]
        for i in range(2,N+1):
            a[i]=min(a[i-1],a[i-2])
            if i<N:a[i]+=cost[i]
        return a[N]
