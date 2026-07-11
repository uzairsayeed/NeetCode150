# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
# The input is generated such that a majority element will exist in the array.
 

# Follow-up: Could you solve the problem in linear time and in O(1) space?

from collections import Counter
class Solution:
    # TC = O(n), SC = O(n)
    def majorityElement1(self, nums: List[int]) -> int:
        n = len(nums)
        majority_ele_freq = 0
        res = -1

        freq_map = Counter(nums)
        # print('freq_map --> ', freq_map)
        for ele, freq in freq_map.items():
            # print('ele, freq --> ', ele, freq)
            if freq > n//2:
                if freq > majority_ele_freq:
                    majority_ele_freq = freq
                    res = ele

        return res
    
    # Optimized Approach (Boyer-Moore Voting Algorithm)
    # Intuition:
        # The problem guarantees that a majority element always exists
        # (frequency > n/2).
        #
        # Imagine repeatedly cancelling one occurrence of the candidate with one
        # occurrence of any different element.
        #
        # Since the majority element appears more times than all other elements
        # combined, it can never be completely cancelled. Therefore, after all
        # possible cancellations, the remaining candidate must be the majority
        # element.
        #
        # 'cnt' represents the number of unmatched occurrences of the current
        # candidate after all cancellations performed so far.
    # TC = O(n)
    # SC = O(1)
    # TC = O(n), SC = O(1)
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        cnt = 0

        for num in nums:
            if cnt == 0:
                candidate = num
                cnt += 1
            else:
                if num == candidate:
                    cnt += 1
                else:
                    cnt -= 1
                    
        return candidate


o = Solution()
# nums = [3,2,3]
nums = [2,2,1,1,1,2,2]
# nums = [6,5,5]
print(o.majorityElement(nums))
