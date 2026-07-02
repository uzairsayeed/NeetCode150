# You are given an array of integers nums, 
# there is a sliding window of size k which is moving from the very left of the array to the very right. 
# You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length




# | Window Type   | Template                                                |
# | ------------- | ------------------------------------------------------- |
# | Variable Size | Expand → While Invalid: Shrink → Update                 |
# | Fixed Size    | Expand → If Window Size == K: Update (if valid) → Slide |
from collections import deque
class Solution:
    # Pattern: Monotonic Queue (Deque)

    # Core Insight:
    # Maintain a deque of indices whose corresponding values are
    # in decreasing order.
    #
    # Why?
    # - The front always stores the maximum of the current window.
    # - Smaller elements behind a larger incoming element can never
    #   become the maximum in the future, so discard them.
    #
    # Elements leave the deque for only two reasons:
    # 1. A larger element arrives -> Remove smaller elements from the BACK.
    # 2. An index falls outside the current window -> Remove it from the FRONT.
    #
    # TC = O(n)
    # SC = O(k)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        start = 0
        res = []

        for end in range(len(nums)):
            # EXPAND : window will contain elements in decreasing order
            while len(window) and nums[end] >= nums[window[-1]]:
                window.pop()
            
            window.append(end)

            # FIX:
            # INVARIANT: if end-satrt=1 == k
            while window and window[0] < start:
                window.popleft()

            if end-start+1 == k:
                res.append(nums[window[0]])
                start += 1

        return res

# Day-1: 02/July/2026
# Notes: was able to crack thje solution , with some minor issues
class Solution:
    def solve(self, nums, k):
        window = deque()
        res = []
        start = 0

        for end in range(len(nums)):
            # EXPAND
            while len(window) and nums[window[-1]] <= nums[end]:
                window.pop()

            window.append(end)

            # Here, we are checking the case where our current window (start -> end) whether it is insync with our deque
            # For example: 
            # window = [1,2,3]
            # start = 2
            # Which means the top of deque(window) can no longer be our answer so we need to make sure our start and window are in sync
            while window and window[0] < start:
                window.popleft()

            if end-start+1 == k:
                res.append(nums[window[0]])
                start += 1

        return res
    
o = Solution()
nums = [3,1,1,3]
k = 3

# nums = [1]
# k = 1
print(o.maxSlidingWindow(nums, k))
