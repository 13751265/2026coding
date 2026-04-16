#week08-2.py
 #給你guess()你可以呼叫他,找出1...n裡面的(答案)
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #另一種寫法
        return bisect_left(range(n+1),0,key=lambda x:-guess(x)) #一行抵下面7行

        #要用小學猜數字(猜數字)每次範圍猜一半,比他大,比她小,縮小範圍
        left,right=0,n #左右的範圍
        while left<right: #左右的範圍還沒有撞再一起
            mid=(left+right)//2  #(猜)中間的數
            if guess(mid)==0:return mid #猜到中間的數字
            if guess(mid)>0: left=mid+1 #暗示你再高一點
            else:right=mid
        return left
