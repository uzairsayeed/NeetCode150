# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

 

# Example 1:


# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:


# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

# Constraints:

# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1
 

# Follow up:

# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

class Solution:
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)

        for row in range(m):
            for col in range(n):
                if row in zero_rows or col in zero_cols:
                    matrix[row][col] = 0
        return matrix


    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_col_zero = False

        for col in range(n):
            if matrix[0][col] == 0:
                matrix[0][0] = 0
        
        for row in range(m):
            if matrix[row][0] == 0:
                first_col_zero = True

        for row in range(1,m):
            for col in range(1,n):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(m):
            for col in range(1,n):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        for col in range(n):
            if matrix[0][0] == 0:
                matrix[0][col] = 0

        for row in range(m):
            if first_col_zero:
                matrix[row][0] = 0
        return matrix
    

    # Day-1: 14/July/2026
    # Intuition:
        # Maintain zero_rows and zero_cols set to track the zeored rows and cols
    # Mistakes Made: 
        # None
    # TC = O(mxn), SC = O(m+n)
    def solve(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)

        for row in range(m):
            for col in range(n):
                if row in zero_rows or col in zero_cols:
                    matrix[row][col] = 0

        return matrix
    
o = Solution()
# matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(o.setZeroes(matrix))
