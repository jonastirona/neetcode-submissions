class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        set_nums = set(nums)
        maximum = 1
        for num in nums:
            if num - 1 not in set_nums and num in set_nums:
                set_nums.remove(num)
                j = 1
                while num + j in set_nums:
                    set_nums.remove(num + j)
                    j+=1

                maximum = max(maximum, j)

        return maximum
