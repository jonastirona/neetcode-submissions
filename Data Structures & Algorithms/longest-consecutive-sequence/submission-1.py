class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums.sort()
        if len(nums) == 0:
            return 0

        longest = 1
        prev = nums[0]
        current = 1
        for num in nums[1:]:
            if num == prev:
                continue
            elif num - 1 == prev:
                current+=1
                longest = max(current, longest)
            else:
                current = 1

            prev = num

        return longest
# [2,3,4,4,5,10,20]