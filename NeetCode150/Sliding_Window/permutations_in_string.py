# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.




# | Window Type   | Template                                                |
# | ------------- | ------------------------------------------------------- |
# | Variable Size | Expand → While Invalid: Shrink → Update                 |
# | Fixed Size    | Expand → If Window Size == K: Update (if valid) → Slide |
from collections import Counter
class Solution:
    # Pattern: Sliding Window
    # Core Insight : The window always has the same size. 
    def checkInclusion1(self, s1: str, s2: str) -> bool:
        c1, c2 = Counter(s1), Counter()
        start = 0

        for end in range(len(s2)):
            # EXPAND
            # We don t need this condition, we can add all the elements regardless. Fixed in below sol
            if s2[end] in c1:
                 c2[s2[end]] += 1

            # INVARIANT : The window size never exceeds len(s1).
            if end-start+1 == len(s1):
                if c1 == c2:
                    return True
                else:
                    # We don t need this condition, we can add all the elements regardless. Fixed in below sol
                    if s2[start] in c1:
                        c2[s2[start]] -= 1
                        if c2[s2[start]] == 0:
                            del c2[s2[start]]
                    start += 1
        return False

    # Pattern: Fixed Size Sliding Window

    # Recognition Trigger:
    # Need to check whether every window of a fixed length
    # satisfies a condition.

    # Core Insight:
    # A permutation must have the same length as the original string.

    # Window Size:
    # len(s1) => FIXED , unlike lengest_repeating_char_replacement and longest_sunstring_wihtout_repeating_char, where the window was VARIABLE

    # Window State:
    # Frequency map of current window.

    # Invariant:
    # Window size never exceeds len(s1).

    # Algorithm:
    # 1. Expand by adding the current character.
    # 2. If window exceeds len(s1), remove the leftmost character.
    # 3. When window size == len(s1), compare frequency maps.

    # TC = O(n)
    # SC = O(1) 
    def checkInclusion2(self, s1: str, s2: str) -> bool:
        c1, c2 = Counter(s1), Counter()
        start = 0

        for end in range(len(s2)):
            # EXPAND
            c2[s2[end]] += 1

            # INVARIANT : The window size never exceeds len(s1).
            if end-start+1 == len(s1):
                if c1 == c2:
                    return True
                else:
                    c2[s2[start]] -= 1
                    if c2[s2[start]] == 0:
                        del c2[s2[start]]
                    start += 1
        return False

    # Day-1: 
    # Notes: Initially i missed that it is a FIXED SLIDING WINDOW type of problem.
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1, c2 = Counter(s1), Counter()
        start = 0

        for end in range(len(s2)):
            # EXPAND
            c2[s2[end]] += 1

            # FIX:
            # Check for the size
            if end-start+1 == len(s1):
                if c1 == c2:
                    return True
                
                else:
                    c2[s2[start]] -= 1
                    if c2[s2[start]] == 0:
                        del c2[s2[start]]

                    start += 1
        return False
o = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(o.checkInclusion(s1, s2))
            
        
