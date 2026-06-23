# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

class Solution:
    def threeSum1(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = set()

        for idx in range(len(nums)-2):
            # Since arr is sorted. If curr_ele > 0 then all the elements are also greater than 0.
            # This their sum can never be 0
            if nums[idx] > 0:
                break
            # print('idx --> ', idx)
            left_ptr, right_ptr = idx+1, len(nums)-1
            # print('left_ptr, right_ptr --> ', left_ptr, right_ptr)

            while left_ptr < right_ptr:
                curr_sum = nums[left_ptr] + nums[right_ptr]
                # print('curr_sum --> ', curr_sum)

                if curr_sum < -nums[idx]:
                    left_ptr += 1
                elif curr_sum > -nums[idx]:
                    right_ptr -= 1
                else:
                    curr_triplet = [nums[idx], nums[left_ptr], nums[right_ptr]]
                    if tuple(curr_triplet) not in res:
                        res.add(tuple(curr_triplet))

                    left_ptr += 1
                    right_ptr -= 1

        return list(res)
    
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums_set = set(nums)
        res = set()


    

o = Solution()
# nums = [-1,0,1,2,-1,-4]
# nums = [0,1,1]
nums = [0,0,0]
print(o.threeSum(nums))
