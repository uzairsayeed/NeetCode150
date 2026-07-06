# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

from collections import Counter
class Solution:
    # Brute-Force: For every idx find the contiguos array that equals K.
    # TC = O(n2) 
    def subarraySum1(self, nums: list[int], k: int) -> int:
        res = 0

        for idx in range(len(nums)):
            curr_sum = nums[idx]
            if curr_sum == k:
                res += 1
            for idx_1 in range(idx+1, len(nums)):
                curr_sum += nums[idx_1]
                if curr_sum == k:
                    res += 1
        return res
    
    # Approach-1: 
    # Pattern : Prefix Sum Array
    # Intuition Building:
        # When we build a prefix sum array, the value at any index 'i' of the prefix_sum array represents the sum of elements till index 'i'
        # prefix_sum[i] = sum (0 ... i) indexes
        # Now if we want sum of any subarray => [l, r] ==> prefix_sum[r] - prefix_sum[l-1]

        # Now problem says : Find subarrays whose sum == k
        # ==> prefix_sum[r] - prefix_sum[l-1] = k
        # For any idx in prefix_sum array we know sum till that point ==> Which means in subarray [l,r] we know 'r' which is our current idx
        # Now we need to find ALL idx's 'l-1' such that for which prefix_sum[r] - k = prefix_sum[l-1]

        # For every current prefix_sum,
        # find how many previous prefix sums equal
        # current_prefix_sum - k
        # Each occurrence corresponds to one valid subarray ending at the current index.
    # TC = O(n)
    # SC = O(n)
    def subarraySum(self, nums: list[int], k: int) -> int:
        res = 0
        prefix_sum = 0
        # Empty prefix before the array starts.
        # This allows us to count subarrays that begin at index 0.
        prefix_cnt = Counter()
        prefix_cnt[0] = 1

        for num in nums:
            prefix_sum += num
            prefix_needed = prefix_sum - k
            if prefix_needed in prefix_cnt:
                res += prefix_cnt[prefix_needed]
            prefix_cnt[prefix_sum] += 1

        return res
o = Solution()
# nums = [1,1,1]
# k = 2

# nums = [1,2,3]
# k = 3

# nums = [28,54,7,-70,22,65,-6]
# k = 100

nums = [1,-1,0]
k = 0
print(o.subarraySum(nums, k))

