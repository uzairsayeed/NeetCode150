# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


class Solution:
    # Day-0: 22/July/2026
    # Recognition Trigger : Pattern Matching, for every open bracket there must be a closing bracket of same type
    # Intuition:
        # Here, stack will store the waiting elements and the waiting elements in this case are
        # OPENING brackets of ALL types
        # Curr element ==> Can it answer the waiting elements?
            # Current closing bracket tries to answer the most recent waiting opening bracket.
            # YES => POP the top element
            # NO => violates the 2nd condition (Open brackets must be closed in the correct order) . So return False
    # TC = O(n), SC = O(n), stack Im not counting map since its storing only 3 values
    # Mistakes Made:
        # None
    def isValid(self, s: str) -> bool:
        res = []
        char_map = {'(':')', '[': ']', '{': '}'}

        for char in s:
            # STACK stoes waiting elements ==> Waiting elements are opening brackets of all the types
            if char in char_map:
                res.append(char)
                print('res-1 --> ', res)

            else:
                print('res-2, char --> ', res, char)

                # This means we need to check whether curr element can answer the waiting elements
                if len(res) and char_map[res[-1]] == char:
                    res.pop()
                    print('res-3 --> ', res)
                else:
                    return False
        print('res --> ', res)
        return False if len(res) else True
    
o = Solution()
# s = "()[]{}"
s = "]"

print(o.isValid(s))
