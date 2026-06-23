# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

class Solution:
    # BF:
    # If I stand on top of bar i,
    # what is the highest wall I can see on my left?
    # what is the highest wall I can see on my right?
    # Finding left_max_ht and right_max_ht for each element
    # Maintain left_max_hts nd right_max_hts
    def trap1(self, height: List[int]) -> int:
        res = 0
        left_max_hts = [-1] * len(height)
        right_max_hts = [-1] * len(height)

        for idx in range(1, len(height)):
            left_max_hts[idx] = max(left_max_hts[idx-1], height[idx-1])
        # print('left_max_hts --> ', left_max_hts)

        for idx in range(len(height)-2, -1, -1):
            right_max_hts[idx] = max(right_max_hts[idx+1], height[idx+1])
        # print('right_max_hts --> ', right_max_hts)

        for idx in range(len(height)):
            if left_max_hts[idx] == -1 or right_max_hts[idx] == -1:
                continue
            else:
                curr_area = min(left_max_hts[idx], right_max_hts[idx]) - height[idx]
                # print('curr_area --> ', curr_area)
                if curr_area > 0:
                    res += curr_area

        return res

        
    def trap(self, height: List[int]) -> int:
        res = 0
        left_ptr, right_ptr = 0, len(height)-1
        left_max, right_max = height[0], height[len(height)-1]

        while left_ptr < right_ptr:
           
            if height[left_ptr] <= height[right_ptr]:
                if height[left_ptr] >= left_max:
                   left_max = height[left_ptr]
                else:
                    res += left_max - height[left_ptr]
                left_ptr += 1
            else:
                if height[right_ptr] >= right_max:
                   right_max = height[right_ptr]
                else:
                    res += right_max - height[right_ptr]
                right_ptr -= 1
                   

        return res


o = Solution()
# height = [4,2,0,3,2,5]
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(o.trap(height))
        