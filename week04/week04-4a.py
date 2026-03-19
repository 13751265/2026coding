#week04-4a.py(重寫week04-2.py)
#找到最高的海拔高度,一直加就好了
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=H=0 #一開始的高度是0
        for gg in gain: #python進階for迴圈:依序取出gg
            H+=gg
            ans=max(ans,H)
        return ans
