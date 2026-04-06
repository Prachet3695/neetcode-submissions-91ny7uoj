class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            count[i] = count.get(i, 0) + 1
        for key_1, v in count.items():
            freq[v].append(key_1)
        
        result = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result

        