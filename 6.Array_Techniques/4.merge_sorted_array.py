# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

# Constraints:

# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109
 

# Follow up: Can you come up with an algorithm that runs in O(m + n) time?


class Solution:
    # Approach: 3 Pointer
    # Intuition:
        # There are two key observations:
            # 1. Both arrays are already sorted.
            # 2. nums1 has exactly n empty slots at the end.

        # Since the free space is at the END of nums1, instead of shifting
        # elements to insert from the front, we merge from the BACK.
        # At every step, compare the largest remaining elements of nums1
        # and nums2. Place the larger one into the last free position.
        # i -> last valid element in nums1
        # j -> last element in nums2
        # k -> last position of nums1 where the next largest element goes
    # TC = O(m+n), SC = O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m-1, n-1, m+n-1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If nums2 still has elements left, copy them.
        # If nums1 has elements left, they're already in the correct position,
        # so nothing needs to be done.
        while j!= -1:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        return nums1
    
o = Solution()
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

# nums1 = [1]
# m = 1
# nums2 = []
# n = 0

nums1 = [0]
m = 0
nums2 = [1]
n = 1
print(o.merge(nums1,m,nums2,n))
        
        
