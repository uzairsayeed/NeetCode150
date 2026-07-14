# Given an array nums with n objects colored red, white, or blue, 
# sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
 

# Follow up: Could you come up with a one-pass algorithm using only constant extra space?

class Solution:
    # Approach : Dutch Flag / 3 Pointers
    # Intuition: 
        # We need to segregate 0's, 1'2 and 2's
        # This implies we'll end up with 4 regions
            # Region 1 : All 0's => [0 to low-1]. 
            # Region 2 : All 1's => [low to mid-1]. 
            # Region 3 : Unknown / Unprocessed Elements => [mid to high]. 
            # Region 4 : All 2's => [high+1 to n-1]. 
        # low => represents the first position where NEXT 0 is to be placed. Everything before low is alrady finalised as 0's
        # high => represents the last position where the next 2 should be placed. Everything after high is alrady finalised as 2's
        # mid => represents the current unknown element being processed
    # Tc = O(n), SC = O(1)
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums)-1
        
        # Continue while there is at least one unprocessed element.
        # The unknown region is [mid ... high] (inclusive),
        # so we stop only when mid > high.
        while mid <= high:
            # 0 belongs in the left region.
            # Swap it into the 0s region and expand both the
            # 0s region and the 1s region.
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
        
            # 2 belongs in the right region.
            # Swap it into the 2s region.
            # Do NOT move mid because the swapped-in element
            # is still unprocessed.
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            
            else:
                # 1 already belongs in the middle region.
                # Simply expand the 1s region.
                mid += 1

        return nums

    # Day-1: 14/July/2026
    # Intuition:
        # Since we need to segregate 0s, 1s and 2s. This can be preocessed as 4 regions
        # Region1 : All 0s => [0 to low -1]. 
        # Region2 : All 1s => [low to mid-1].
        # Region3 : Current / Unprocessed elements => [mid to high]
        # Region4 : All 2s => [high+1 to n-1]
        # low => represents the first position where NEXT 0 is to be placed. Everything before low is alrady finalised as 0's
        # high => represents the last position where the next 2 should be placed. Everything after high is alrady finalised as 2's
        # mid => represents the current unknown element being processed
    # Mistakes Made:
        # None
    # Tc = O(n), SC = O(1)
    def solve(self, nums: List[int]) -> List[int]:
        n = len(nums)
        low, mid, high = 0, 0, n-1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
            else:
                mid += 1
        return nums

o = Solution()
# nums = [2,0,2,1,1,0]
nums = [2,0,1]
print(o.sortColors(nums))
        
