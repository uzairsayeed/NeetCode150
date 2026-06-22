# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.



class Solution:
    # My intitial solution: Issue here is we are upfront building the map , 
    # which can cause issues in case there are duplicate values in the array.
    def two_sum1(self, nums: List[int], target: int) -> List[int]:
        res = []
        nums_map = {val:idx for idx, val in enumerate(nums)}
        # print('nuyms_map --> ', nums_map)
        for idx, ele in enumerate(nums):
            curr = target-ele
            # print('curr ->', curr)
            if curr in nums_map and idx != nums_map[curr]:
                res.extend([idx, nums_map[curr]])
                break
        
        return res
        

    # Instead of building the map upfront, build it dynamically as you iterate through the list. 
    # Check if the complement exists in the map before adding the current number. 
    # This completely avoids the duplicate overwrite bug and eliminates the need for the idx != nums_map[curr] check.
    def two_sum2(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for idx, ele in enumerate(nums):
            curr = target - ele
            # print('curr --> ', curr)
            if curr in nums_map:
                return [nums_map[curr], idx]
            
            nums_map[ele] = idx
            # print('nums_map --> ', nums_map)


        return []


    # Day-1: 18/June/2026
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        res = []
        idx_map = {}

        for idx in range(len(nums)):
            curr = target - nums[idx]
            
            if curr in idx_map:
                res.extend([idx_map[curr], idx])
                break
            
            idx_map[nums[idx]] = idx

        return res






nums = [3,3]
target = 6
o = Solution()
print(o.two_sum(nums, target))
