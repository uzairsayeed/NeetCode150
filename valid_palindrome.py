# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.


class Solution:
    def isPalindrome1(self, s: str) -> bool:
        res = True
        sanitised_str_arr = []

        for char in s:
            if char.isalnum():
                sanitised_str_arr.append(char.lower())

        # print(sanitised_str_arr)

        return sanitised_str_arr == sanitised_str_arr[::-1]
    

    # This approach uses O(n) extra memory
    def isPalindrome1(self, s: str) -> bool:
        res = True
        sanitised_str_arr = []

        for char in s:
            if char.isalnum():
                sanitised_str_arr.append(char.lower())

        # print(sanitised_str_arr)

        left_ptr, right_ptr = 0, len(sanitised_str_arr)-1
        
        while left_ptr <= right_ptr:
            if sanitised_str_arr[left_ptr] != sanitised_str_arr[right_ptr]:
                res = False
                break
            left_ptr += 1
            right_ptr -= 1

        return res
    
    # This approach uses no extra space.
    def isPalindrome(self, s: str) -> bool:
        res = True
        left_ptr, right_ptr = 0, len(s)-1

        while left_ptr <= right_ptr:
            # print('left_ptr --> ', left_ptr)
            # print('right_ptr --> ', right_ptr)

            if not s[left_ptr].isalnum():
                left_ptr += 1

            elif not s[right_ptr].isalnum():
                right_ptr -= 1

            elif s[left_ptr].lower() == s[right_ptr].lower():
                left_ptr += 1
                right_ptr -= 1

            else:
                res = False
                break

        return res
       



o = Solution()
s = "A man, a plan, a canal: Panama"
# s = "race a car"
# s = ' '
print(o.isPalindrome(s))