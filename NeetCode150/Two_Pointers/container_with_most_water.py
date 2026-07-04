# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104


class Solution:
    # BF: For every height find its area with every other hbeight while maintaining the trail
    # TC = O(n2)
    def maxArea1(self, height: list[int]) -> int:
        res = 0

        for x in range(len(height)):
            for y in range(x+1, len(height)):
                curr_ht = min(height[x], height[y])
                curr_wd = y - x
                curr_area = curr_ht * curr_wd

                res = max(res, curr_area)

        return res
    
    
    def maxArea2(self, height: list[int]) -> int:
        res = 0
        left_ptr, right_ptr = 0, len(height)-1

        while left_ptr < right_ptr:
            curr_ht = min(height[left_ptr], height[right_ptr])
            curr_wd = right_ptr - left_ptr
            curr_area = curr_ht * curr_wd
            res = max(res, curr_area)

            if height[left_ptr] <= height[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1
    
        return res
    
    # Day-1: 24/June/2026
    # Pattern: Two POinter
    # Trigger: By keeping left, right = 0, len(height)-1, weve already maximised the width
    # Inorder to max height the side with shorter height needs to be moved
    # Notes: was able to solve the problem.
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left_ptr, right_ptr = 0, len(height)-1

        while left_ptr < right_ptr:
            curr_area = min(height[left_ptr], height[right_ptr]) * (right_ptr-left_ptr)
            res = max(res, curr_area)

            if height[left_ptr] <= height[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1

        return res

    # Day-07: 03/July/2026
    # Notes: I was able to crack the intuition in first go and solved it .
    # Mistakes Made: While calculating width, inititally i did (right_ptr-left_ptr+1)
    def solve(self, height: list[int]) -> int:
        res = 0
        left_ptr, right_ptr = 0, len(height)-1

        while left_ptr < right_ptr:
            if height[left_ptr] <= height[right_ptr]:
                res = max(res, height[left_ptr] * (right_ptr-left_ptr))
                left_ptr += 1
            else:
                res = max(res, height[right_ptr] * (right_ptr-left_ptr))
                right_ptr -= 1
        return res

o = Solution()
# height = [1,8,6,2,5,4,8,3,7]
height = [1,1]
print(o.maxArea(height))
