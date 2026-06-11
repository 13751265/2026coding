class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1]) #氣球照右邊界排序
        ans=0
        previous_end=-inf
        for start,end in points: #逐一取出氣球
            if previous_end<start: #氣球有距離喔!只好再多射一箭
                ans+=1 #要為現在的[start,end]的氣味,射一箭
                previous_end=end
        return ans
