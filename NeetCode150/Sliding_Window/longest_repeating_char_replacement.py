# You are given a string s and an integer k. 
# You can choose any character of the string and change it to any other uppercase English character. 
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

from collections import Counter
class Solution:
    # Approach:
    # EXPAND the window 
    # FIX the window-> Invariant [window_size - max_frequency > k] will make the window INVALID
    # UPDATE the answer.
    # Pattern: Sliding Window (Frequency Map)
    # TC = O(n)
    # SC = O(1)   # Uppercase English letters   
    def characterReplacement1(self, s: str, k: int) -> int:
        window = Counter()
        start = 0
        max_len = 0

        for end in range(len(s)):
            # EXPAND STEP
            window[s[end]] += 1
            # print('window-1 --> ', window)
            # FIX STEP
            if len(window) > 1:
                max_char_freq = max(window.values())
                # print('max_char_freq-1 --> ', max_char_freq)

                replacement_needed = sum(window.values()) - max_char_freq
                # print('replacement_needed-1 --> ', replacement_needed)

                if replacement_needed > k:
                    window[s[start]] -= 1
                    start += 1
            
            # UPDATE
            max_len = max(max_len, end-start+1)
            # print('-------------------------------------------------------------------------')

        return max_len
    

    # MISSES:
    # 1. It should be while, not if
    # Always follow the sliding window template . Though IF worked in this case its better to stick to the stanbdard template.
    # FIX Step ==> while invalid:
    #                   shrink()
    # 2. Delete characters whose count becomes zero.
    def characterReplacement(self, s: str, k: int) -> int:
        window = Counter()
        start = 0
        max_len = 0

        for end in range(len(s)):
            # EXPAND STEP
            window[s[end]] += 1
            # FIX STEP
            if len(window) > 1:
                max_char_freq = max(window.values())
                replacement_needed = sum(window.values()) - max_char_freq

                if replacement_needed > k:
                    window[s[start]] -= 1
                    if window[s[start]] == 0:
                        del window[s[start]]
                    start += 1
            
            # UPDATE
            max_len = max(max_len, end-start+1)
            # print('-------------------------------------------------------------------------')

        return max_len
    

o = Solution()
# s = "ABAB"
# k = 2

s = "AABABBA"
k = 1

# s= "ABAA"
# k = 0
print(o.characterReplacement(s, k))
        
