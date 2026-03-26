#week05-5.py
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1=Counter(word1)
        counter2=Counter(word2)

        #用過的字母,是否是相同的組合(左邊有,右邊也有)
        if set(counter1.keys()) != set(counter2.keys()):
            return False
        #把出現的次數,小到大排好,如果兩邊都一樣,那就可以換到一樣為止
        if sorted(counter1.values()) != sorted(counter2.values()):
            return False
        return True
