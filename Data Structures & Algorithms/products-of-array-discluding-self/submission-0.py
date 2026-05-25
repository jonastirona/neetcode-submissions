class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        products = [1 for i in range(len(nums))]

        for i in range(len(nums)):
            for j in range(len(products)):
                if i == j: continue
                products[i]*=nums[j]
        
        return products