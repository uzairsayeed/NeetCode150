# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

# Example 1:

# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
# Example 2:

# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
# Example 3:

# Input: nums = [23,2,6,4,7], k = 13
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# 0 <= sum(nums[i]) <= 231 - 1
# 1 <= k <= 231 - 1

class Solution:
    # Pattern: Prefix Sum + HashMap
    # Intuition Building:
        # Can the subarray represented as difference of prefix_sum's ==> If YES ==> Then PREFIX SUM is the right approach Not SLIDING WINDOW
        # Any subarray sum => prefixsum[r]-prefixsum[l-1]
        # A good subarray muist satisfy below TWO conditions
        # 1. len(subarray) > 2
        # 2. prefixsum[r] - prefixsum[l-1] % k = 0 => prefixsum[r]%k = prefixsum[l-1]%k ==> We'll search whether prefixsum[r]% k exists or not
        # Which means instead of storing prefix sums in the hashmap ==> we'll store prefixsum%k in map
        # Also to handle cases where %k value is zero ==> set map with {0:-1}
    # Mistakes made:
        # 1. Missed the %k = 0 case
        # 2. Also I was updating the already seen idexes ==> earliest occurrence always gives the longest subarray.
        
        # Why earliest index?
        # If the same remainder appears multiple times, the earliest occurrence
        # produces the longest possible subarray, maximizing the chance of
        # satisfying the length >= 2 condition.

        # Initialization:
        # prefix_map = {0: -1}
        # Represents the empty prefix before the array starts.
        # This correctly handles subarrays beginning at index 0.
    # TC = O(n), SC = O(n)

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = 0
        prefix_map = {0:-1}
        req_prefix_len = 2

        for idx in range(len(nums)):
            prefix_sum += nums[idx]
            prefix_needed = prefix_sum % k

            if prefix_needed in prefix_map:
                prefix_len = idx - prefix_map[prefix_needed]
                if prefix_len >= req_prefix_len:
                    return True
            else:
                prefix_map[prefix_needed] = idx

        return False
        
    
o = Solution()
# nums = [23,2,6,4,7]
# k = 6

# nums = [23,2,6,4,7]
# k = 13

# nums = [23,2,4,6,6]
# k = 7

nums = [5,0,0,0]
k = 3
print(o.checkSubarraySum(nums, k))
