class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxima = 0
        seen = set()
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])

            maxima = max(maxima, r-l+1)

        
        return maxima


