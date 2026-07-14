# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
# More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
# then the next permutation of that array is the permutation that follows it in the sorted container. 
# If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

class Solution:
    # Pattern:
    # Intuition:
        # # We need the lexicographically next permutation,
        # i.e., the smallest permutation that is larger than the current one.
        # So the problem boils down to "Finding a number which is greater than the current number immediately"
        # Inorder to find such combination, from where do we start => from LEFT(Most Significant Position) or from RIGHT(Least Significant Position)
        # Since we are finding the smallest largest number , e can only get that by starting from RIGHT (Units place) not from left.
        # So we start from RIGHT ==> Should we satrt from n-1 or n-2 index?
        # It should be from n-2 index since we need some number to swap, so start from immediate left of units place.
        # Now we must find the PIVOT => nums[i] < nums[i+1] ==> This ensures that the descending order is breaking at PIVOT position.
        # Once PIVOT is obtained swap it with smallest element greater than the pivot
        # After SWAP, reverse all the numbers right TO THE PIVOT INDEX, to obtain the smallest possible arrangement.
    def nextPermutation(self, nums: List[int]) -> None:
        pivot_idx = -1

        for idx in range(len(nums)-2,-1,-1):
            if nums[idx] < nums[idx+1]:
                pivot_idx = idx
                break
        if pivot_idx != -1:
            # Since the first element which is greater than pivot , is the smallest greatest number than pivot as the part right to pivot is already descending in nature
            for idx in range(len(nums)-1, pivot_idx, -1):
                if nums[pivot_idx] < nums[idx]:
                    nums[pivot_idx], nums[idx] = nums[idx], nums[pivot_idx]
                    break

            left, right = pivot_idx+1, len(nums)-1
            while left < right:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1
        else:
            left, right = 0, len(nums)-1
            while left < right:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1
        return nums
    
    # Day-1: 14/July/2026
    # Intuition:
        # The problem says to find the next lexicographically greater permutation of its integer
        # which is nothing but the NEXT immediate larger number than the provided one
        # Inorder to find the NEXT immediate larger number which position must be considred to begin with ?
            # Is it Most Significant Position or the Least Significant Position (UNITS Place) 
            # It should be LSP not MSP, if we start with MSP it wont lead to the NEXT immediate larger no
            # Inorder to get the next immediate larger number , it must be the LSP
        # Starting from LSP, if we encounter an element where nums[idx] < nums[idx+1] ==> This is where the pivot exists
        # Once pivot_index is obtained => Find the smallest number which is larger than the pivot_element and SWAP it with
        # Next just reverse the part whcih is RIGHT to pivot_index
    # TC = O(n), SC = O(1)
    # Mistakes Made:
        # Was able to crack the logic
    def solve(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pivot_index = -1

        # We start from the Least Significant Position (UNITS Place)
        for idx in range(n-2, -1, -1):
            if nums[idx] < nums[idx+1]:
                pivot_index = idx
                break

        if pivot_index != -1:
            # Find the smallest largest number than pivot element
            for idx in range(n-1, -1, -1):
                if nums[idx] > nums[pivot_index]:
                    nums[idx], nums[pivot_index] = nums[pivot_index], nums[idx]
                    break
    
        # Now reverse the list right to pivot_index
        left, right = pivot_index+1, n-1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums
o = Solution()
# nums = [1,2,5,4,3]
# nums = [3,2,1]
nums = [1,5,2,3,1]


print(o.nextPermutation(nums))
        
