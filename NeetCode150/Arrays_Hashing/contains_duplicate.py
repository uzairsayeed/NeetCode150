# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true

 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution:
    def containsDuplicate1(self, nums: List[int]) -> bool:
        nums_set =set()
        for ele in nums:
            if ele in nums_set:
                return True
            nums_set.add(ele)
        return False
    
    # Instead of looping manually using a Python for loop, you can convert the entire list into a set all at once and compare their lengths:
    def containsDuplicate2(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


    # Day-1: 18/June/2026
    # Pattern: Set/Counter
    # Recognition Trigger: Check for the freq>1 for any element
    # Brute Force: Two loops. 1st loop fixed the curr ele and 2nd loop check for the occurrence of same element. O(n2)
    # Optimization Insight: Can use a set/Counter
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))