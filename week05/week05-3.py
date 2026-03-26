#week05-3.py
#–贺计,瞷Ω计ゲ斗常ぃ妓
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter=Counter(arr)#参璸计瞷Ω计
        s=set()
        for c in counter:#盢计硋ㄓ
            #print(c,counter[c])  #计,瞷碭Ω
            if counter[c]in s: #狦Τ瞷筁,ア毖
                return False
            s.add(counter[c])#瞷硂瞷Ω计,s柑
        return True #繦獽return
