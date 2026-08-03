# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
 

# Constraints:

# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

class Solution:
    # Day-0: 23/July/2026
    # Recognition Trigger: Postfix / Reverse Polish Expression Evaluation
    # Intuition:
        # Maintain a stack of operands.
        # Whenever an operand (number) is encountered, push it onto the stack.
        # Whenever an operator is encountered, pop the top two operands, apply the operator, and push the result back.
        # Each intermediate result becomes an operand for future operations.
    # TC = O(n), SC = O(n). Since allowed_operators map contains only 4 values
    def evalRPN(self, tokens: List[str]) -> int:
        # In this we'll be STORING numbers and are WAITING for an operator
        element_stack = []
        allowed_operators = {'+', '-', '*', '/'}

        for ele in tokens:
            if ele in allowed_operators:
                op2 = element_stack.pop()
                op1 = element_stack.pop() 

                if ele == '+':
                    element_stack.append(op1+op2)
                elif ele == '-':
                    element_stack.append(op1-op2)
                elif ele =='*':
                    element_stack.append(op1*op2)
                else:
                    res = op1/op2
                    element_stack.append(int(res))
            else:
                element_stack.append(int(ele))
        return element_stack[0]


    # Day-7: 02/Aug/2026
    # Recognition Trigger: Expression Evaluation
    # Pattern: Stack
    # Intuition:
        # Push elements into the stack and when operator is encountered pop 2 elements and insert the resultant back into the stack]
    # Mistakes Made:
        # None
    def solve(self, tokens: list[str]) -> int:
            stack = []
            operators = ["+", "-", "*", "/"]
    
            for ele in tokens:
                if ele not in operators:
                    stack.append(int(ele))
                else:
                    op2 = stack.pop()
                    op1 = stack.pop()
    
                    if ele == '+':
                        stack.append(op1 + op2)
                    elif ele == '-':
                        stack.append(op1 - op2)
                    elif ele == '*':
                        stack.append(op1 * op2)
                    else:
                        res = op1/op2
                        stack.append(int(res))
            return stack[-1]

o = Solution()
# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# tokens = ["4","13","5","/","+"]
# tokens = ["2","1","+","3","*"]
tokens = ["0","3","/"]
print(o.evalRPN(tokens))            
