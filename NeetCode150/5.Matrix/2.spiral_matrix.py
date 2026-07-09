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
