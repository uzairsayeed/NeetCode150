# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m-1
        left, right = 0, n-1

        while top <= bottom and left <= right:
            # Add top row from left -> right
            for col in range(left, right+1):
                res.append(matrix[top][col])
            top += 1

            # Add right column from top -> bottom
            for row in range(top, bottom+1):
                res.append(matrix[row][right])
            right -= 1

            # Add bottom row from right -> left
            if top <= bottom:
                for col in range(right, left-1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # Add left column from left -> right
            if left <= right:
                for row in range(bottom, top-1, -1):
                    res.append(matrix[row][left])
                left += 1

            # print(res)
            # print('top, bottom --> ', top, bottom)
            # print('left, right --> ', left, right)

        return res
    

    class Solution:
    # Day-1: 14/July/2026
    # Intuition: 
        # To print spiral we need to move in 4 directions and must initalise the boundary vars
        # top, bottom = 0, rows-1
        # left, right = 0, cols-1
        # Since there are lements at 1,1 2,2 .. so we should be using equality in the WHILE condition
        # Adding elements from left to right => Then that TOP row is done ==> So increment the TOP var
        # Adding elements from top to bottom => Then that RIGHT col is done ==> So decrement the RIGHT var
        # Adding elements from right to left => Then that BOTTOM row is done ==> So decrement the BOTTOM var
        # Adding elements from bottom to top => Then that LEFT col is done ==> So increment the LEFT var

    # Mistakes Made:
        # Was able to determine the core logic and changing of the boundary vars
        # Missed the equality cosnition in WHILE loop
        # For every direction , the FOR loop condition was going till m/n/0 , which is wrong
        # Missed the [if top <= bottom] and [if left <= right] conditions.

    def solve(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m-1
        left, right = 0, n-1
    
        res = []

        while top <= bottom and left <= right:
            # Adding elements from left to right
            for col in range(left, right+1):
                res.append(matrix[top][col])

            top += 1

            # Adding elements from top to bottom
            for row in range(top, bottom+1):
                res.append(matrix[row][right])

            right -= 1

            # Adding elements from right to left
            if top <= bottom:
                for col in range(right, left-1, -1):
                    res.append(matrix[bottom][col])
            
                bottom -= 1

            # Adding elements from bottom to top
            if left <= right:
                for row in range(bottom, top-1, -1):
                    res.append(matrix[row][left])
            
                left += 1

        return res
    
o = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(o.spiralOrder(matrix))
