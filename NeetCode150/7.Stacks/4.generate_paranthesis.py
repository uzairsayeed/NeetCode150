# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8


class Solution:
    # 1. Base case: Is the answer complete?
    # 2. Check every possible choice.
    # 3. Make a legal choice.
    # 4. Recurse.
    # 5. Undo the choice.

    # Choice: '('
    # Legal when: open_count < n

    # Choice: ')'
    # Legal when: close_count < open_count

    # Complete when: open_count == close_count == n
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current: str, open_count: int, close_count: int) -> None:
            # Complete answer: used all n opening and n closing brackets
            if open_count == n and close_count == n:
                result.append(current)
                return

            # Choice 1: Add '(' when openings are still available
            if open_count < n:
                backtrack(
                    current + "(",
                    open_count + 1,
                    close_count
                )

            # Choice 2: Add ')' only when an unmatched '(' exists
            if close_count < open_count:
                backtrack(
                    current + ")",
                    open_count,
                    close_count + 1
                )

        backtrack("", 0, 0)
        return result
