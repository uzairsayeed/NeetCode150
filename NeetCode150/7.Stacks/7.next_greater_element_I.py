# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. 
# If there is no next greater element, then the answer for this query is -1.

# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

# Example 1:

# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# Example 2:

# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 

# Constraints:

# 1 <= nums1.length <= nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 104
# All integers in nums1 and nums2 are unique.
# All the integers of nums1 also appear in nums2.
 

# Follow up: Could you find an O(nums1.length + nums2.length) solution?



class Solution:
    # Day-0: 04/Aug/2026
    # Recognition Pattern: FOr every element of nums1 we need to find next greater element present in nums2.
    # Pattern: Monotonic Stack
    # Intuition:
        # We can apply the next greater element logic on nums2 but with one modification
        # Since we need to find next greater element of only those elements of nums2 that are in nums1
        # Create an idx map of nums1 and while popping elements from stack
        # check whether the popped element is part of nums1
        # Since only nums1 elements can contribute to our final answer
    # TC = O(n+m), n = len(nums1), m = len(nums2)
    # Mistakes Made:
        # None
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        idx_map = {}
        for idx,num in enumerate(nums1):
            idx_map[num] = idx
            
        stack = []

        for idx,num in enumerate(nums2):
            while stack and stack[-1] < num:
                popped_ele = stack.pop()
                if popped_ele in idx_map:
                    popped_ele_idx = idx_map[popped_ele]
                    res[popped_ele_idx] = num

            stack.append(num)

        return res

o = Solution()
# nums1 = [4,1,2]
# nums2 = [1,3,4,2]   

nums1 = [2,4]
nums2 = [1,2,3,4]
print(o.nextGreaterElement(nums1, nums2))
