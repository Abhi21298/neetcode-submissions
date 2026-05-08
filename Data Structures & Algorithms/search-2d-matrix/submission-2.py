class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row_l = 0
        row_r = len(matrix) - 1 
        col_l = 0
        col_r = len(matrix[0]) - 1

        while row_l <= row_r:
            mid_r = (row_l + row_r) // 2

            if target < matrix[mid_r][col_l]:
                row_r = mid_r - 1
            elif target > matrix[mid_r][col_r]:
                row_l = mid_r + 1
            else:
                break
        
        while col_l <= col_r:
            mid_c = (col_l +  col_r) // 2

            if target == matrix[mid_r][mid_c]:
                return True
            elif target < matrix[mid_r][mid_c]:
                col_r = mid_c - 1
            else:
                col_l = mid_c + 1
        
        return False

        