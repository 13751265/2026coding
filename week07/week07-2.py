#week07-1.py
#正的向右,負的向左,大的會把小的消滅,一樣大一起死
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans=[]
        for a in asteroids:
            if a>0: #正的往右,不會跟左邊的相撞
                ans.append(a) #直接塞()
            else: #負的往左,可能會取ans裡的東西相撞很多次
                while ans and  ans[-1]>0: #目前有存,且最右邊正的,向右,會相撞
                    if abs(ans[-1])==abs(a): #絕對值大小很相同,都消滅
                        ans.pop() #消滅了,吐掉
                        a=0 #也消滅了
                        break #離開迴圈
                    elif abs(ans[-1])>abs(a):
                        a=0
                        break
                    else:
                        ans.pop()
                if a != 0: ans.append(a)
        return ans
