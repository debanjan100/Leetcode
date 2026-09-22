class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        rotated = []
        for i in range(len(matrix)): 
            rows = []
            for j in range(len(matrix)):
                rows.append(matrix[j][i])
            rotated.append(rows[::-1])
        matrix [:]= rotated