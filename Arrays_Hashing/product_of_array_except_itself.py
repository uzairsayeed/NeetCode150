# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105 => ALLOWED TC can be at max O(nlogn)
# -30 <= nums[i] <= 30 => Negatives are also present
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

# Observations:
# 1. => ALLOWED TC can be at max O(nlogn)
# 2. => Negatives are also present

class Solution:
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        res = []
        for idx in range(len(nums)):
            curr_product_left = 1 
            curr_product_right = 1

            # To calculate the product of nums to the right except itself 
            for idx1 in range(idx+1, len(nums)):
                curr_product_right *= nums[idx1]

            # To calculate the product of nums to the left except itself
            for idx2 in range(idx-1,-1, -1):
                curr_product_left *= nums[idx2]

            # print('curr --> ', nums[idx])
            # print('curr_product_left --> ', curr_product_left)
            # print('curr_product_right --> ', curr_product_right)

            res.append(curr_product_left * curr_product_right)

        return res
    


    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)

        prefix_prdt = [1]*len(nums)
        prefix_prdt[0] = nums[0]
        for idx in range(1,len(nums)):
             curr = nums[idx] * prefix_prdt[idx-1]
             prefix_prdt[idx] = curr

        postfix_prdt = [1] * len(nums)
        postfix_prdt[len(nums)-1] = nums[len(nums)-1]
        for idx in range(len(nums)-2, -1, -1):
             curr = nums[idx] * postfix_prdt[idx+1]
             postfix_prdt[idx] = curr

        # print('prefix_prdt --> ', prefix_prdt)
        # print('postfix_prdt --> ', postfix_prdt)

        for idx in range(len(nums)):
            if idx == 0:
                res[idx] = 1 * postfix_prdt[idx+1]
            elif idx == len(nums)-1:
                res[idx] = prefix_prdt[idx-1] * 1
            else:
                res[idx] = prefix_prdt[idx-1] * postfix_prdt[idx+1]

        return res
    

    def productExceptSelf3(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)

        prefix_prdt = 1
        postfix_prdt = 1

        for idx in range(len(nums)):
            res[idx] = prefix_prdt
            prefix_prdt = prefix_prdt * nums[idx]

        for idx in range(len(nums)-1, -1, -1):
            res[idx] = postfix_prdt * res[idx]
            postfix_prdt = postfix_prdt * nums[idx]

        return res
    

    def productExceptSelf3(self, nums: List[int]) -> List[int]:
        res = [1]* len(nums)
        prefix, postfix = 1, 1

        for idx in range(len(nums)):
            res[idx] = prefix
            prefix = prefix * nums[idx]
        print(res)
        for idx in range(len(nums)-1, -1, -1):
            res[idx] = postfix * res[idx]
            postfix = postfix * nums[idx]

        return res
    

    # Day-1: 18/June/2026
    # Pattern: prefix and postfix array
    # Recognition Trigger: Toi get prdt of array except element itself => rightPrdt x leftPrdt
    # Brute Force: Two loops. O(n2)
    # Optimization Insight: Instead of creating 2 seperate arrays for prefix and postfix , use the output arr
    def productExceptSelf4(self, nums: List[int]) -> List[int]:
        prefix_prdt = [1]*len(nums)
        prefix_prdt[0] = nums[0]
        for idx in range(1,len(nums)):
            prefix_prdt[idx] = prefix_prdt[idx-1] * nums[idx]

        postfix_prdt = [1]*len(nums)
        postfix_prdt[len(nums)-1] = nums[len(nums)-1]
        for idx in range(len(nums)-2, -1, -1):
            postfix_prdt[idx] = postfix_prdt[idx+1] * nums[idx]

        print('prefix_prdt --> ', prefix_prdt)
        print('postfix_prdt --> ', postfix_prdt)

        res = [1]*len(nums)
        for idx in range(len(nums)):
            print('idx --> ', idx)
            if idx == 0:
                res[idx] = postfix_prdt[idx+1]
            elif idx == len(nums)-1:
                res[idx] = prefix_prdt[idx-1]
            else:
                res[idx] = prefix_prdt[idx-1] * postfix_prdt[idx+1]
        return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prefix_prdt = 1
        postfix_prdt = 1

        for idx in range(0,len(nums)):
            res[idx] = prefix_prdt
            prefix_prdt = prefix_prdt * nums[idx]

        for idx in range(len(nums)-1, -1, -1):
            res[idx] = postfix_prdt * res[idx]
            postfix_prdt = postfix_prdt * nums[idx]
        return res
o = Solution()
nums = [-1,1,0,-3,3]
# nums = [1,2,3,4]

print(o.productExceptSelf(nums))

