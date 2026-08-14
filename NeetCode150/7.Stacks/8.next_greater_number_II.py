# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), 
# return the next greater number for every element in nums.

# The next greater number of a number x is the first greater number to its traversing-order next in the array, 
# which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 

# Example 1:

# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number. 
# The second 1's next greater number needs to search circularly, which is also 2.
# Example 2:

# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]
 

# Constraints:

# 1 <= nums.length <= 104
# -109 <= nums[i] <= 109


class Solution:
    # Day-0: 04/Aug/2026
    # Recognition Trigger: For every element we need to find next greater element
    # Pattern: Stack
    # Intuition:
        # This problem is same as nexxt greater element but here we have a circular array
        # Let's understand the curcular array
            #  5 4 3 2 1 -> 5 4 3 2 1
            # By looking can we say every element will find answer 
                # Either to its right => by travelling from left to right
                # OR
                # By to its left => while travelling from left to right
                # By that logic, can we say if we double the array , we can mimick the 2 iterations
                # And also , even if we traverse the 3rd or 4th ..or nth time it wont make any difference .
                # Since in 2 iterations we are covering the left to right and right to left part.
                # Which is enough to say that no element needs to be visited more than twice
            # Thus, we can iterate over 2n instead of n and in single iteration we can find the answer for every element 
    # TC = O(2n)
    # SC = O(n)
    # Mistakes Made:
        # Was not able to crack the circular array logic of 2n
        # With the hint was able top code it 
        # Rate: 3/5
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        res = [-1] * len(nums)

        for idx in range(2*n):
            actual_index = idx % n
            while stack and nums[stack[-1]] < nums[actual_index]:
                popped_idx = stack.pop()
                res[popped_idx] = nums[actual_index]

            stack.append(actual_index)

        return res

    # <<<<<<<<<<<<<<<< CLEANER VERSION , TC = O(n) >>>>>>>>>>>>>>>>>
    # Day-0: 04/Aug/2026

    # Recognition Trigger:
        # For every element, find the first greater element to its right
        # in a circular array.

    # Pattern:
        # Monotonic Stack + Circular Traversal

    # Intuition:
        # The stack stores original indices that are still waiting for
        # their next greater element.
        #
        # A circular array can be simulated by traversing 2n positions:
        #
        #     actual_index = idx % n
        #
        # First lap:
        #     Process every original element and add unresolved indices
        #     to the stack.
        #
        # Second lap:
        #     Revisit the beginning of the array so unresolved elements
        #     can find answers after wrapping around.
        #
        # During the second lap, do not push indices again because they
        # already represent the original elements waiting in the stack.

    # TC = O(n)
    # SC = O(n)

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        for idx in range(2 * n):
            actual_index = idx % n

            while (
                stack
                and nums[stack[-1]] < nums[actual_index]
            ):
                waiting_index = stack.pop()
                result[waiting_index] = nums[actual_index]

            if idx < n:
                stack.append(actual_index)

        return result

    # Day-7: 13/Aug/2026
    # Recognition Pattern: For every eloement find trhe next greater element
    # Pattern: Stack
    # Intuition:
        # It is same as finding next greater elemetn, the only catch is the circular array part
        # That can be handled if we traverse from 0 -> 2n instead of n
        # At every idx of the traversal, we'll calculate curr_idx 
            # curr_idx = idx if idx < n else idx%n
        # Then the same logic opf next greater element is to be applied.
    # TC = O(n), SC = O(n)
    # Mistakes Made:
        # None
        # rating: 5/5
    def solve(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        res = [-1] * n

        for idx in range(2*n):
            curr_idx = idx%n
            while stack and nums[stack[-1]] < nums[curr_idx]:
                res[stack.pop()] = nums[curr_idx]

            if idx < n:
                stack.append(curr_idx)

        return res
o = Solution()
nums = [1,2,1]
# nums = [1,2,3,4,3]
# nums = [5,4,3,2,1]
print(o.nextGreaterElements(nums))
