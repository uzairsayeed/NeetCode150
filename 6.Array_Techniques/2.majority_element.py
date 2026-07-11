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
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority_ele_freq = 0
        res = -1

        freq_map = Counter(nums)
        # print('freq_map --> ', freq_map)
        for ele, freq in freq_map.items():
            # print('ele, freq --> ', ele, freq)
            if freq >= n//2:
                if freq > majority_ele_freq:
                    majority_ele_freq = freq
                    res = ele

        return res
o = Solution()
# nums = [3,2,3]
# nums = [2,2,1,1,1,2,2]
nums = [6,5,5]
print(o.majorityElement(nums))
