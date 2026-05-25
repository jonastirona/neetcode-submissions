class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        for i in range(0, len(nums) - 2):
            for j in range(1, len(nums) - 1):
                for k in range(2, len(nums)):
                    if i == j or j == k or i == k:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        triple = sorted([nums[i], nums[j], nums[k]])
                        if triple not in triplets:
                            triplets.append(triple)







        return list(triplets)