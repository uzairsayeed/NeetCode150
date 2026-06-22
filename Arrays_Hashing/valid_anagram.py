# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?




from collections import Counter
class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) >= len(t):
            return len(Counter(s) - Counter(t)) == 0
        return len(Counter(t) - Counter(s)) == 0

    # Day-1: 18/June/2026
    # Pattern: Counter
    # Recognition Trigger: Check for the char freqs
    # Brute Force: Two loops. O(n2)
    # Optimization Insight: Can use a Counter
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


o = Solution()
s = "anagram"
t = "nagaram"

print(o.isAnagram(s,t))
