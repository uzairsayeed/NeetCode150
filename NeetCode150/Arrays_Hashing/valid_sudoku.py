# 36. Valid Sudoku

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

from collections import Counter
class Solution:
    def isValidSudoku1(self, board: List[List[str]]) -> bool:
        res = True

        def isRowAndColValid(start_idx: int) -> bool:
            row_set = set()
            col_set = set()

            for idx in range(9):
                curr_row_ele = board[start_idx][idx]
                curr_col_ele = board[idx][start_idx]

                if curr_row_ele != '.':
                    if curr_row_ele not in row_set:
                        # print('curr_row_ele --> ', curr_row_ele)
                        row_set.add(board[start_idx][idx])
                    else:
                        return False
                    
                if curr_col_ele != '.':
                    if curr_col_ele not in col_set:
                        # print('curr_col_ele --> ', curr_col_ele)
                        col_set.add(board[idx][start_idx])
                    else:
                        return False
                    

            return True
        
        def is3x3GridValid(grid_coordinates: List[List[int]]) -> bool:
            r_start, c_start = grid_coordinates[0]
            r_end, c_end = grid_coordinates[1]

            grid_set = set()
            for r in range(r_start, r_end+1):
                for c in range(c_start, c_end+1):
                    curr_ele = board[r][c]
                    # print('curr_ele --> ', curr_ele)

                    if curr_ele != '.':
                        if curr_ele not in grid_set:
                            grid_set.add(curr_ele)
                            # print('grid_set --> ', grid_set)

                        else:
                            return False
            return True
        
        for idx in range(9):
            # print('curr_idx --> ', idx)
            res = isRowAndColValid(idx)
            if not res:
                return res
            
        grid_start_end_idx_arr = [
            [[0,0], [2,2]],
            [[0,3], [2,5]],
            [[0,6], [2,8]],
            [[3,0], [5,2]],
            [[3,3], [5,5]],
            [[3,6], [5,8]],
            [[6,0], [8,2]],
            [[6,3], [8,5]],
            [[6,6], [8,8]]
        ]
            
        for grid in grid_start_end_idx_arr:
            # print('gird --> ', grid)
            res = is3x3GridValid(grid)
            # print('res --> ', res)
            if not res:
                return res
        return res
            

    # Optimised Approach: 
        # 1. Remove Hardcoded 3×3 Grid Coordinates => Map every element to each of the 9 boxes 
        # 2. Single Traversal Instead of Three Traversals => Check all 3 conditions in single pass
        # 3. Compute Box Index Instead of Iterating Boxes ==> box_idx = (r//3)*3+(c//3)
        # 4. Use Three Arrays of Sets for rows,cols and boxes
    # Optimisation Insight : Create array of sets for each row , col and box

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = True
        rows_set = [set() for _ in range(9)]
        cols_set = [set() for _ in range(9)]
        boxes_set = [set() for _ in range(9)]

        # print('rows_set --> ', rows_set)
        # print('cols_set --> ', cols_set)
        # print('boxes_set --> ', boxes_set)

        for r in range(9):
            for c in range(9):
                # print('r, c --> ', r, c)
                curr = board[r][c]

                if curr == '.':
                    continue

                box_idx = (r//3) * 3 + (c//3)

                if (
                    curr in rows_set[r] or
                    curr in cols_set[c] or
                    curr in boxes_set[box_idx]
                ):
                    res = False
                    break

                rows_set[r].add(curr)
                cols_set[c].add(curr)
                boxes_set[box_idx].add(curr)

        return res


o = Solution()

# board = [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]


# board = [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

board = [
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]
]

print(o.isValidSudoku(board))
