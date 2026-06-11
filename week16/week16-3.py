class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #intervals.sort() #先排序,依據右邊的結束時間
        intervals.sort(key=lambda x:x[1]) #用右邊的大小來排序
        ans=0
        previous_end=-inf
        for start,end in intervals: #逐一取出[start,end]
            if previous_end <= start: #沒有重疊
                previous_end=end
            else:
                ans+=1
        return ans
