class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        m_rows, n_cols = len(matrix), len(matrix[0])
        low_ptr, high_ptr = 0, (m_rows * n_cols) - 1
        
        while low_ptr <= high_ptr:
            middle_idx = low_ptr + (high_ptr - low_ptr) // 2
            curr_row, curr_col = divmod(middle_idx, n_cols)
            current_val = matrix[curr_row][curr_col]
            
            if current_val == target:
                return True
            elif current_val < target:
                low_ptr = middle_idx + 1
            else:
                high_ptr = middle_idx - 1
                
        return False
