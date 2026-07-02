class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            if matrix[row][-1] < target:
                continue
            else:
                for col in range(len(matrix[row])):
                    if matrix[row][col] == target:
                        return True
        return False 