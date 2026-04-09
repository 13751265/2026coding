#week07-4.py
#將字串解碼 數字代表(重複的次數)會把右邊方括號裡的字串重複
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[] #利用stack處理方括號及對英的數字
        nowN,nowS=0,'' #左邊N數字vs.右邊nowS字串
        for c in s:
            if c.isdigit(): #若是數字,就用十進位組合起來
                nowN=nowN*10+int(c)
            elif c.isalpha(): #如果是字母 就讓字母便長
                nowS+=c
            elif c=='[': #上括號:數字,字串放入stack
                stack.append((nowN,nowS))
                nowN,nowS=0,'' #一組新的數字,字串
            elif c==']': #下括號:取出數字,字母
                prevN,prevS=stack.pop()
                nowS=prevS+prevN*nowS #重複的次數,字串
        return nowS
