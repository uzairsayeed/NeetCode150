# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:


# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

# | Transformation     | Operations                                                      |
# | -------------------| --------------------------------------------------------------- |
# | 90° Clockwise      | Transpose → Reverse each row                                    |
# | 90° Anti-clockwise | Transpose → Reverse each column                                 |
# | 180° Rotation      | Reverse rows → Reverse columns (or reverse the flattened array) |
# | Transpose          | Swap `(i, j)` with `(j, i)`                                     |

# Complexity:
# TC = O(n²)
# SC = O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 90° clockwise rotation can be decomposed into:
        # 1. Transpose (rows ↔ columns)
        # 2. Reverse every row
        for r in range(len(matrix)):
            for c in range(r, len(matrix[r])):
                matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c]
        
        # Now reverse each row 
        for r in range(len(matrix)):
            matrix[r].reverse()

    # Day-1: 13/July/2026
    # Inuition:
        # Transpose the given matrix ==> rows to cols ==> matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        # Reverse each row ==> Use list.reverse() - operates in-place and does not create a new list.
    # Notes:
        # I was able to solve it in single go.
        # While transposing the given matrix , I we go all the from 0 to rows and 0 to cols, the transpose will be nullified
        # Instead go from 0 to rows and row to cols
    # Mistakes Made:
        # None
    def solve(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])

        # Transpose of the matrix
        for row in range(m):
            for col in range(row, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # Reverse each row
        for row in range(m):
            matrix[row].reverse()

o = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(o.rotate(matrix))
