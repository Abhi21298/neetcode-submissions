class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])
        
        # finding the row first
        top, bottom = 0, rows - 1
        while top <= bottom:
            target_row = (top + bottom) // 2
            if target < matrix[target_row][0]:
                bottom -= 1
            elif target > matrix[target_row][-1]:
                top += 1
            else:
                break
            
        if top > bottom:
            return False
        
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            if target < matrix[target_row][m]:
                r -= 1
            elif target > matrix[target_row][m]:
                l += 1
            else:
                return True
        
        return False

        