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
    # Pattern : Prefix Sum + HashMap (Frequency Map)
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
    

    # Day-1: 07/July/2026
    # Pattern: Prefix Sum + Counter
    # Notes: I was ble to get thje intuition and solve the problem in single take.
    def solve(self, nums: list[int], k: int) -> int:
        res = 0
        prefix_sum = 0
        prefix_cntr = Counter()
        # Inorder to handle the case for prefix_sum[0] => At 0th index
        prefix_cntr[0] = 1

        for num in nums:
            # Calculate prefix sum on the fly
            prefix_sum += num
            # How we dervice at (prefix_sum-k) ??
            # When we build a prefix_sum array ==> Any index 'i' of that array represents sum of elements from 0th index till ith index
            # If Ive to find prefix sum of a subarray with start,end indexes as [l,r], It would be 
                #  prefix_sum[r] - prefix_sum[l-1]
            # Now let's us cosnider the given problem statement => FIND ALL SUBARRAY'S WHOSE SUM = K
                # => We need to find ALL 
                # => prefix_sum[r] - prefix_sum[l-1] = k
            # If we are index 'i' , it means we have already calculated prefix_sum's till 'i' index and we know all the prev prefix_Sum's
                # => We know 'r' and doin't know 'l-1'
                # => prefix_sum[r] - k = prefix_sum[l-1]
            # Since we have already calculated ALL prefix_sums till 'r' , we can simply search whether (prefix_sum[l-1]) exists in our computed prefixes or not
            # We need to get the cnt of ALL such (prefix_sum[r] - k) from the computed prefix_sum's
            prefix_needed = prefix_sum - k
            if prefix_needed in prefix_cntr:
                res += prefix_cntr[prefix_needed]

            # Update the counter with our current prefix_sum
            prefix_cntr[prefix_sum] += 1

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

