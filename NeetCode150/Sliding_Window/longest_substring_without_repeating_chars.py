# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.



# | Window Type   | Template                                                |
# | ------------- | ------------------------------------------------------- |
# | Variable Size | Expand → While Invalid: Shrink → Update                 |
# | Fixed Size    | Expand → If Window Size == K: Update (if valid) → Slide |
class Solution:
    # Approach 1: This approach passed on leetcode but its not the optimal sliding window solution.
    # Hrfe we are clearing the set on every trigger which is not optimal
    # Instead of clearing the set , we should re-use the already processed elements
    # Pattern: Set + Sliding Window
    # Recognition Trigger: Inorder to calculate the longest substring without repeating chars, the sliding window must be maintained
    # TC = O(n)
    def lengthOfLongestSubstring1(self, s: str) -> int:
        # print('len --> ', len(s))
        if len(s) == 0 or len(s) == 1:
            return len(s)
        max_len = 0
        substring_set = set()
        start, end = 0, 1
        substring_set.add(s[start])

        while end < len(s):
            # print('start, end --> ', start, end)
            # print('substring_set-1 --> ', substring_set)

            if s[end] not in substring_set:
                substring_set.add(s[end])
                end += 1
            else:
                # print('substring_set-2 --> ', substring_set)

                max_len = max(max_len, len(substring_set))
                start += 1
                substring_set.clear()
                substring_set.add(s[start])
                end = start + 1
        # print('substring_set-3 --> ', substring_set)
        if len(substring_set):
            max_len = max(max_len, len(substring_set))
        return max_len
    

    def lengthOfLongestSubstring2(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_len = 0
        window_set = set()
        window_set.add(s[0])

        start, end = 0, 1

        while end < len(s):
            if s[end] not in window_set:
                window_set.add(s[end])
                end += 1

            else:
                while s[end] in window_set:
                    max_len = max(max_len, len(window_set))
                    window_set.remove(s[start])
                    start += 1

                window_set.add(s[end])
                max_len = max(max_len, len(window_set))
                end += 1

        if len(window_set):
            max_len = max(max_len, len(window_set))
        return max_len


    def lengthOfLongestSubstring3(self, s: str) -> int:
        window_set = set()
        start = 0
        max_len = 0

        for end in range(len(s)):

            # 1. Expand Window
            while s[end] in window_set:

                # 2. Fix Window
                window_set.remove(s[start])
                start += 1

            window_set.add(s[end])

            # 3. Update Answer
            max_len = max(max_len, end - start + 1)

        return max_len
    
    # Day-1: 26/June/2026
    # Pattern : Sliding Window
    # Core Insight:
    # Fix the window => If we encounter a duplicate , fix the window -> make it valid by removing the duplicate and update the start ptr
    # Expand the window => By addind the incoming element which actually was the cause of FIX
    # Update the answer 
    def lengthOfLongestSubstring4(self, s: str) -> int:
        window_set = set()
        start = 0
        max_len = 0

        for end in range(len(s)):
            # Fix the window
            while s[end] in window_set:
                window_set.remove(s[start])
                start += 1

            # Expand the window
            window_set.add(s[end])

            # Update the answer
            max_len = max(max_len, end-start+1)

        return max_len

    # IMPORTANT:
    # We update max_len only AFTER the Fix step because only VALID windows
    # are candidates for the answer.
    #
    # During the Fix step, the window contains duplicate characters,
    # so any window size observed at that point is invalid and cannot
    # contribute to the answer.
    #
    # Once the duplicate is completely removed, the window invariant
    # is restored:
    #     "All characters in the window are unique."
    #
    # We then expand the window by adding the current character and
    # update the answer using the size of this valid window.
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        start = 0
        max_len = 0

        for end in range(len(s)):           
            # FIX STEP
            # Invariant => Curr element is already present in window making it invalid
            while s[end] in window:
                window.remove(s[start])
                # SHRINK the window
                start += 1

            # EXPAND
            window.add(s[end])
            # UPDATE
            max_len = max(max_len, end-start+1)


        return max_len
    
    # Day-07: 03/July/2026
    # Notes: I was able to crack thje intuition, found the valid and invalid window state 
    # Mistakes Made:
    # 1. Same mistake as Day-1, during the FIX step when we encountered curr_ele to be duplicate I was immediately calculating 'res'
    # The reason why it shouldnt be calculated is, as we are currently processing s[end] and it turns out to be alrady present in window 
    # It makes the window invalid.
    # Hence , first FIX the window , then INSERT the curr_ele into the window and then calculate res
    def solve(self, s: str) -> int:
        res = 0
        start = 0
        window = set()

        for end in range(len(s)):
            # FIX
            # Invariant => Current ele is part of the window already
            while s[end] in window:
                window.remove(s[start])
                start += 1

            window.add(s[end])

            res = max(res, end-start+1)


        return res
o = Solution()
s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
# s = ''
# s = " "
# s = 'au'
# s = 'dvdf'
print(o.lengthOfLongestSubstring(s))
            
