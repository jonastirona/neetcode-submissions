class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        numss = set(nums)
        longest = 0
        for num in numss:
            if num - 1 in numss: continue
            else:
                temp = 1
                while num + 1 in numss:
                    num = num + 1
                    temp += 1

                longest = max(longest, temp)

        return longest