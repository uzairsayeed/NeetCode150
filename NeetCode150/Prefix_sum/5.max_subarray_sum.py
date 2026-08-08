# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104

# Kadane's Algorithm:
# curr_sum = max(num, curr_sum + num)
# answer = max(answer, curr_sum)

class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        res = float('-inf')
        min_seen_so_far = float('inf')
        prefix_sum = 0

        for num in nums:
            min_seen_so_far = min(min_seen_so_far, prefix_sum)
            prefix_sum += num
            res = max(res, prefix_sum - min_seen_so_far)

        return res
    
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        curr_sum = 0

        for num in nums:
            curr_sum = max(curr_sum+num, num)
            res = max(res, curr_sum)

        return res


    # Day-7: 08/Aug/2026
        # REcognityion Trigger: SUbarray Sum
        # Pattern: Prefix Sum / Kadane's Algorithm
        # Intuition:
            # Prefix Sum Approach:
                # Any subarray [l,r] sum can be represented as prefix_sum[r] - prefix_sum[l-1]
                # In this problme we want : (preix_sum[r] - prefix_sum[l-1]) to be max
                # => prefix_sum[r] can be MAX if we find prefix_sum[l-1] to be MIN
                # So we compute : "min_prefix_sum_seen_so_far"
                # Then we compute max_prefix_sum
        # TC = O(n), SC = O(1)
        # Mistakes Made:
            # Needed help to trigger the intuition
            # Rating : 3/5
    def solve(self, nums: List[int]) -> int:
        prefix_sum = 0
        min_prefix_sum_seen_so_far = float('inf')
        max_prefix_sum = float('-inf')

        for idx,num in enumerate(nums):
            min_prefix_sum_seen_so_far = min(min_prefix_sum_seen_so_far, prefix_sum)
            prefix_sum += num
            max_prefix_sum = max(max_prefix_sum, prefix_sum - min_prefix_sum_seen_so_far)
            
        return max_prefix_sum
    
    # Day-7: 08/Aug/2026
        # REcognityion Trigger: SUbarray Sum
        # Pattern: Prefix Sum / Kadane's Algorithm
        # Intuition:
            # Kadane's Algorithm:
                # We compute running SUM
                # At every idx, we have to options either to continue with the RUNNING SUM or just considere the CURR ELEMENT 
                # Since nums can be negative as well, we need to pick the MAX of (RUNNING SUM, CURR ELEMENT)
                # Then we compute the "max_prefix_sum"
        # TC = O(n), SC = O(1)
        # Mistakes Made:
            # Needed help to trigger the intuition
            # Rating : 3/5
    def solve(self, nums: List[int]) -> int:
        max_prefix_sum = float('-inf')
        curr_sum = 0

        for num in nums:
            curr_sum = max(num, curr_sum + num)
            max_prefix_sum = max(max_prefix_sum, curr_sum)

        return max_prefix_sum
