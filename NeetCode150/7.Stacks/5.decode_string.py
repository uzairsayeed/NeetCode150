# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. 
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
# For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

 

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
 

# Constraints:

# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].

class Solution:
    # Day-0: 02/Aug/2026
    # Recognittion Trigger : Expression evaluation
    # Pattern: Stack
    # Intuition:
        # Which elements can be considered as WAITING elements?
            # Excpet ']', rest are all waiting elements
        # So push waiting elements into the stack
        # When ']' is encounbtered it can answer the WAITING elemets
            # First , we'll formualte the current valid str , then we calculate thge freq of the current valid str
            # Then insert back the resultant into the stack
    # Mistakes Made:
        # None
    # TC = O(n + decoded_output_size)
    # SC = O(n + decoded_output_size)
    def decodeString(self, s: str) -> str:
        stack = []

        for ele in s:

            if ele == ']':
                curr_elements = []
                while stack[-1] != '[':
                    curr_elements.append(stack.pop())

                curr_elements.reverse()
                curr_str = ''.join(curr_elements)

                # This will pop out '['
                stack.pop()

                # This will pop integer
                freq = []
                while stack and isinstance(stack[-1], int):
                    freq.append(str(stack.pop()))

                freq.reverse()
                freq_cnt = int(''.join(freq))
                
                res = []
                while freq_cnt:
                    res.append(curr_str)
                    freq_cnt -= 1

                stack.append(''.join(res))
            else:
                if (ele == '[') or (ord(ele) >= 97 and ord(ele) <= 122):
                    stack.append(ele)
                else:
                    stack.append(int(ele))
        return ''.join(stack)


class Solution:
    # Pattern:
    # Stack — Nested Expression Evaluation

    # Recognition Trigger:
    # Nested encoded sections where the most recently opened section
    # must be resolved first.

    # Intuition:
    # The stack stores unresolved characters and encoding context.
    # When ']' arrives, the most recent encoded section is complete:
    # 1. Pop characters until '[' to build the current substring.
    # 2. Remove '['.
    # 3. Pop all preceding digits to build the repeat count.
    # 4. Decode the substring and push it back.
    #
    # The decoded result may itself belong to an outer encoded section.

    # TC = O(n + decoded output size)
    # SC = O(n + decoded output size)

    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(int(char) if char.isdigit() else char)
                continue

            encoded_chars = []

            while stack[-1] != "[":
                encoded_chars.append(stack.pop())

            stack.pop()  # Remove '['
            encoded_chars.reverse()
            encoded_string = "".join(encoded_chars)

            digits = []

            while stack and isinstance(stack[-1], int):
                digits.append(str(stack.pop()))

            digits.reverse()
            repeat_count = int("".join(digits))

            stack.append(encoded_string * repeat_count)

        return "".join(stack)


    # Day-7: 14/Aug/2026
    # Recognition Pattern: Pattern Matching
    # Pattern: Stack
    # Intuition:
        # Push waiting elements => waiting elements : [, digits and alphabets
        # If ']' is encountered
            # Pop the alphabets => create the curr str
            # Pop the ]
            # Pop the digits => form the cnt numeric
            # Create the str * cnt => insert back to the stack
    # TC = O(n + decoded_output_size)
    # SC = O(n + decoded_output_size)
    # Mistakes Made:
        # None
        # Rating: 5/5
    def solve(self, s: str) -> str:
        char_stack = []

        for char in s:
            # When to POP ?
            # If char is "]" , it answers the elements in waiting
            if char == ']':
                curr_str_arr = []
                # First, get the chars for the str
                while char_stack and char_stack[-1] != '[':
                    curr_str_arr.append(char_stack.pop())

                # Pop '['
                char_stack.pop()

                # Form, the number
                curr_char_cnt_arr = []
                while char_stack and char_stack[-1].isdigit():
                    curr_char_cnt_arr.append(char_stack.pop())


                curr_char_cnt_arr.reverse()
                curr_char_cnt = int(''.join(curr_char_cnt_arr))

                curr_str_arr.reverse()
                curr_str = ''.join(curr_str_arr)
                char_stack.append(curr_str * curr_char_cnt)

            else:
                # What to INSERT ?
                # The below are the elements in waiting in stack
                # Digits, Alphabets and [ 
                char_stack.append(char)

        return ''.join(char_stack)

o = Solution()
# s = "3[z]2[bc]"
# s = "3[a2[c]]"
s = "2[abc]3[cd]ef"
# s = "100[leetcode]"
print(o.decodeString(s))
