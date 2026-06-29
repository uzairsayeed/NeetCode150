# Given two strings s and t of lengths m and n respectively, 
# return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
# If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
 

# Follow up: Could you find an algorithm that runs in O(m + n) time?



# | Window Type   | Template                                                |
# | ------------- | ------------------------------------------------------- |
# | Variable Size | Expand → While Invalid: Shrink → Update                 |
# | Fixed Size    | Expand → If Window Size == K: Update (if valid) → Slide |
from collections import Counter
class Solution:
    # Approach 1:
    # Expand
    #    ↓
    # Window becomes VALID
    #    ↓
    # While VALID:
    #     Update answer
    #     Shrink
    #    ↓
    # Window becomes INVALID
    #    ↓
    # Expand again
    # TC = O(m · n)
    def minWindow1(self, s: str, t: str) -> str:
        c1, c2 = Counter(), Counter(t)
        start = 0
        min_len = float('inf')
        res = ''

        for end in range(len(s)):
            # EXPAND
            c1[s[end]] += 1
            # print('c1 --> ', c1)
            # print('start, end --> ', start, end)
            # FIX:
            # INVARIANT: Current window contains every character of t.
            # As long as that's true => keep shrinking. => The moment it becomes false, => expand again. 
            while not (c2-c1):
                # UPDATE
                if min_len > end-start+1:
                    min_len = end-start+1
                    res = s[start:end+1]
                    # print('min_len, res --> ', min_len, res)

                #SHRINK:
                c1[s[start]] -= 1
                if c1[s[start]] == 0:
                    del c1[s[start]]
                start += 1
                
                # This is redundant as the outer loop is already taking char of shrinking
                while start < len(s) and s[start] not in c2:
                    c1[s[start]] -= 1
                    if c1[s[start]] == 0:
                        del c1[s[start]]
                    start += 1
            # print('-------------------------------------------------------------------------')
            # print('start, end-2 --> ', start, end)
        
        return res
    

    def minWindow2(self, s: str, t: str) -> str:
        c1, c2 = Counter(), Counter(t)
        start = 0
        min_len = float('inf')
        res = ''

        for end in range(len(s)):
            # EXPAND
            c1[s[end]] += 1
            # FIX:
            # INVARIANT: Current window contains every character of t.
            # As long as that's true => keep shrinking. => The moment it becomes false, => expand again. 
            while not (c2-c1):
                # UPDATE
                if min_len > end-start+1:
                    min_len = end-start+1
                    res = s[start:end+1]

                #SHRINK:
                c1[s[start]] -= 1
                if c1[s[start]] == 0:
                    del c1[s[start]]
                start += 1
                
        return res
        
    # Pattern: Variable Size Sliding Window
    # Core Insight:
    # Expand until the current window contains all characters of t.
    # Once valid, keep shrinking to find the minimum valid window.
    #
    # have = Number of characters whose required frequency has been satisfied.
    # need = Total number of unique characters whose frequency needs to be satisfied.
    #
    # TC = O(m + n)
    # SC = O(n)

    def minWindow3(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        target = Counter(t)
        window = Counter()

        have = 0
        need = len(target)

        start = 0
        min_len = float("inf")
        res = ""

        for end in range(len(s)):

            # =====================
            # 1. EXPAND
            # =====================
            window[s[end]] += 1

            # Check if current character's required frequency is satisfied
            if s[end] in target and window[s[end]] == target[s[end]]:
                have += 1

            # =====================
            # 2. SHRINK WHILE VALID
            # =====================
            while have == need:

                # Update answer
                if end - start + 1 < min_len:
                    min_len = end - start + 1
                    res = s[start:end + 1]

                # Remove leftmost character
                window[s[start]] -= 1

                # Did removing it break the requirement?
                if (
                    s[start] in target
                    and window[s[start]] < target[s[start]]
                ):
                    have -= 1

                start += 1

        return res
    
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        c1, c2 = Counter(), Counter(t)
        start = 0
        have, need = 0, len(c2)
        min_len = float('inf')
        res = ''

        for end in range(len(s)):
            # EXPAND
            c1[s[end]] += 1

            if s[end] in c2 and c1[s[end]] == c2[s[end]]:
                have += 1

            # FIX
            # IF WINDOW IS VALID ==> SHRINK
            while have == need:
                if min_len > end-start+1:
                    min_len = end-start+1
                    res = s[start:end+1]

                # Till this point window is valid ==> So now SHRINK
                c1[s[start]] -= 1

                # As we removed the leftmost element from the window
                # Now check ==> does this removal made the window INVALID
                if s[start] in c2 and c1[s[start]] < c2[s[start]]:
                    have -= 1

                # Increment the start
                start += 1

        return res



o = Solution()
s = "ADOBECODEBANC"
t = "ABC"

# s = "aa"
# t = "a"
print(o.minWindow(s, t))
