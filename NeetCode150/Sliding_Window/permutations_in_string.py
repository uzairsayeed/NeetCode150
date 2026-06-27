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

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1, c2 = Counter(s1), Counter()
        start = 0

        for end in range(len(s2)):
            # EXPAND
            if s2[end] in c1:
                 c2[s2[end]] += 1

            # INVARIANT
            if end-start+1 == len(s1):
                if c1 == c2:
                    return True
                else:
                    if s2[start] in c1:
                        c2[s2[start]] -= 1
                        if c2[s2[start]] == 0:
                            del c2[s2[start]]
                    start += 1
            

        return False


o = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(o.checkInclusion(s1, s2))
            
        
