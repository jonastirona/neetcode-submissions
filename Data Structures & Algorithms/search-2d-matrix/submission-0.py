class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y = len(matrix[0])
        x = len(matrix)
        length = x*y

        left, right = 0, length-1

        while left <= right:
            mid = left + (right - left) // 2
            r = mid // y
            c = mid - (r*y)
            
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False