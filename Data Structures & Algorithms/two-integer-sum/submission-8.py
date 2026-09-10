class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_1 = {}
        
        for ind, num in enumerate(nums):
            complement = target - num
            if complement in dict_1:
                return [dict_1[complement], ind]
            dict_1[num]= ind
        