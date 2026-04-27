class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            count = [0]*26 # Will act as key, that we can append relevant values to
            for char in word:
                count[ord(char) - ord('a')] += 1
            groups[tuple(count)].append(word) # count is list, and it cannot be key
        
        return list(groups.values())



        
