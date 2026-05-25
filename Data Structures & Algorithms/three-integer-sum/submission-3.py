class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(0, len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                triple = nums[i] + nums[left] + nums[right]
                if triple == 0:
                    if [nums[i], nums[left], nums[right]] not in triplets:
                        triplets.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                elif triple < 0:
                    left+=1
                else:
                    right-=1

        return triplets