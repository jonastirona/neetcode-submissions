class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = ((right - left) // 2) + left
            print(f"mid: {mid}")

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
                print(f"left array, left: {left}, right: {right}")
            elif nums[mid] > target:
                right = mid - 1
                print(f"right array, left: {left}, right: {right}")
        return -1