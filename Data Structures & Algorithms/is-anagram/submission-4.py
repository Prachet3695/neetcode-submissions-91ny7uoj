class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_1 = {}
        count_2 = {}
        for ch in s:
            if ch in count_1:
                count_1[ch] += 1
            else:
                count_1[ch] = 1
        
        for ch in t:
            if ch in count_2:
                count_2[ch] += 1
            else:
                count_2[ch] = 1
        
        if count_1 == count_2:
            return True
        return False