# https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        lower_col, upper_col, lower_row, upper_row, spiral_matrix = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        length_array = (upper_col + 1) * (upper_row + 1)
        
        while len(spiral_matrix) != length_array:
            for index in range(lower_col, upper_col + 1):
                spiral_matrix.append(matrix[lower_row][index])
            
            lower_row += 1
            if len(spiral_matrix) == length_array: return spiral_matrix 
            for index in range(lower_row, upper_row + 1):
                spiral_matrix.append(matrix[index][upper_col])
            
            upper_col -= 1
            if len(spiral_matrix) == length_array: return spiral_matrix 
            for index in range(upper_col, lower_col - 1, -1):
                spiral_matrix.append(matrix[upper_row][index])
            
            upper_row -= 1
            if len(spiral_matrix) == length_array: return spiral_matrix     
            for index in range(upper_row, lower_row - 1, -1):
                spiral_matrix.append(matrix[index][lower_col])
            
            lower_col += 1
            
            print(spiral_matrix)
            
        return spiral_matrix
        
