# You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

# The length of the subarray is k, and
# All the elements of the subarray are distinct.
# Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,5,4,2,9,9,9], k = 3
# Output: 15
# Explanation: The subarrays of nums with length 3 are:
# - [1,5,4] which meets the requirements and has a sum of 10.
# - [5,4,2] which meets the requirements and has a sum of 11.
# - [4,2,9] which meets the requirements and has a sum of 15.
# - [2,9,9] which does not meet the requirements because the element 9 is repeated.
# - [9,9,9] which does not meet the requirements because the element 9 is repeated.
# We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
# Example 2:

# Input: nums = [4,4,4], k = 3
# Output: 0
# Explanation: The subarrays of nums with length 3 are:
# - [4,4,4] which does not meet the requirements because the element 4 is repeated.
# We return 0 because no subarrays meet the conditions.
 

# Constraints:

# 1 <= k <= nums.length <= 105
# 1 <= nums[i] <= 105



# | Window Type   | Template                                                |
# | ------------- | ------------------------------------------------------- |
# | Variable Size | Expand → While Invalid: Shrink → Update                 |
# | Fixed Size    | Expand → If Window Size == K: Update (if valid) → Slide |

from collections import Counter
class Solution:
    # This solution lead to TLE as we are always computing SUM
    def maximumSubarraySum1(self, nums: List[int], k: int) -> int:
        window = Counter()
        start = 0
        max_sum = 0

        for end in range(len(nums)):
            print('start, end --> ', start, end)
            # EXPAND
            window[nums[end]] += 1
            print('window --> ', window)

            # FIX
            # INVARIANT : If current window is of size K but numbers in it are not distinct. This will make the window INVALID . So FIX
            while end-start+1 == k and len(window) != k:
                window[nums[start]] -= 1
                if window[nums[start]] == 0:
                    del window[nums[start]]
                start += 1
                print('start, end-1 --> ', start, end)
                print('window-1 --> ', window)


            # UPDATE: by this point the window will contain only distinct nums. So check the condition and UPDATE
            if end-start+1 == k and len(window) == k:
                max_sum = max(max_sum, sum(nums[start:end+1]))
                window[nums[start]] -= 1
                if window[nums[start]] == 0:
                    del window[nums[start]]
                start += 1

        return max_sum
    

    # TC = O(n)
    # SC = O(k)
    def maximumSubarraySum2(self, nums: List[int], k: int) -> int:
        window = Counter()
        start = 0
        max_sum, curr_sum = 0, 0


        for end in range(len(nums)):
            # EXPAND
            window[nums[end]] += 1
            curr_sum += nums[end]

            # FIX
            # INVARIANT : If current window is of size K but numbers in it are not distinct. This will make the window INVALID . So FIX
            while end-start+1 == k and len(window) != k:
                window[nums[start]] -= 1
                curr_sum -= nums[start]

                if window[nums[start]] == 0:
                    del window[nums[start]]
                start += 1

            # UPDATE: by this point the window will contain only distinct nums. So check the condition and UPDATE
            if end-start+1 == k and len(window) == k:
                max_sum = max(max_sum, curr_sum)
                window[nums[start]] -= 1
                curr_sum -= nums[start]
                if window[nums[start]] == 0:
                    del window[nums[start]]
                start += 1

        return max_sum
    
    # Cleanr Solution
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = Counter()
        start = 0
        max_sum, curr_sum = 0, 0


        for end in range(len(nums)):
            # EXPAND
            window[nums[end]] += 1
            curr_sum += nums[end]

            # FIX
            # INVARIANT : If current window is of size K but numbers in it are not distinct. This will make the window INVALID . So FIX
            while end-start+1 == k:
                # UPDATE
                if len(window) == k:   
                    max_sum = max(max_sum, curr_sum)

                # SLIDE WINDOW
                window[nums[start]] -= 1
                curr_sum -= nums[start]

                if window[nums[start]] == 0:
                    del window[nums[start]]

                start += 1

        return max_sum
    

o = Solution()
nums = [1,5,4,2,9,9,9]
k = 3

# nums = [4,4,4]
# k = 3

# nums = [5,3,3,1,1]
# k = 3
print(o.maximumSubarraySum(nums, k))
