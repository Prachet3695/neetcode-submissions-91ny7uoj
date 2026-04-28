class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            ind = []
            for j in range(len(nums)):
                if j != i:
                    ind.append(j)
                    j += 1
            
            product = 1
            for i in ind:
                product *= nums[i]

            res.append(product)
        
        return res



