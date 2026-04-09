#week07-5.py
class RecentCounter:

    def __init__(self): #一開始物件的建構子,只呼叫一次
        self.queue=deque()
        #使用queue的資料結構

    def ping(self, t: int) -> int:
        self.queue.append(t) #從右邊塞入一個數
        while self.queue[0]<t-3000: #(目前最左邊,為古老的t)超過範圍
            self.queue.popleft() #python的左邊吐掉
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
