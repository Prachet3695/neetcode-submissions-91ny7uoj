class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashish = {}
        for i in nums:
            hashish[i] = hashish.get(i, 0) + 1
        hashish = sorted(hashish.items(), key = lambda x: x[1], reverse=True)

        list_1 = []
        for i in range(k):
            list_1.append(hashish[i][0])
        
        return list_1