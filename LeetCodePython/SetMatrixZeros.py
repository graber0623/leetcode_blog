from collections import defaultdict
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix[0])
        n = len(matrix)
        rowd = defaultdict(int)
        cold = defaultdict(int)
        for i in range(m):
            for j in range(n):
                if matrix[j][i] == 0:
                    rowd[i] = 1
                    cold[j] = 1

        for i in range(m):
            for j in range(n):
                if rowd[i] or cold[j]:
                    matrix[j][i] = 0

        