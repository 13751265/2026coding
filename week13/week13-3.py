class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #先用作弊寫法解一次
        #nums.sort(reverse=True)
        #return nums[k-1]

        heapify(nums)
        for i in range(len(nums)-k):
            heappop(nums)
        return heappop(nums)
