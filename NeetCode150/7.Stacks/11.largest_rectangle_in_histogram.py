# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
# return the area of the largest rectangle in the histogram.

# Example 1:
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.


# Example 2:
# Input: heights = [2,4]
# Output: 4
 

# Constraints:
# 1 <= heights.length <= 105
# 0 <= heights[i] <= 104



class Solution:
    # Day-0: 06/Aug/2026
    # Recognition Pattern: For every histogram bar, determine how far it can extend left and right before encountering a smaller bar. 
        # Think Monotonic Increasing Stack.
    # Pattern: Stack (Monotonic)
    # Intuition:
        # Stack contains indices of bars in non-decreasing height order.
        # Every bar in the stack is waiting for its first smaller bar on the right.
        # When a smaller bar arrives:
            # current index = exclusive right boundary
            # new stack top after pop = exclusive left boundary
            # width = right - left - 1
        # Bars remaining after traversal never found a smaller bar on the right,
        # so use len(heights) as their exclusive right boundary.
    # TC = O(n), SC = O(n)
    # Notes:
        # 1. Could not initially derive that each bar waits for a smaller bar, not a greater bar.
        # 2. Confused the left-boundary index with the distance from the popped bar.
        # 3. Needed to understand that the new stack top after popping reveals the nearest smaller bar on the left.
    # Rating: 2.5/5
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for idx,height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                right_boundary = idx

                popped_idx = stack.pop()
                # current idx is its first smaller bar on the right;
                # the new stack top is its first smaller bar on the left;
                # therefore, the rectangle occupies everything between them.
                left_boundary = stack[-1] if stack else -1

                curr_width = right_boundary - left_boundary - 1
                curr_height = heights[popped_idx]

                curr_area = curr_width * curr_height

                max_area = max(max_area, curr_area)

            stack.append(idx)

        # This is to handle the case, where the elements in the stack didnt encountered any smaller elemetrns to its rgiht
        # So this marks as the lastIndex+1 as the final RIGHT boundary
        # NOw for every element of the stack we figure out the LEFT boundary 
        # And we then calculate the area
        while stack:
            popped_idx = stack.pop()
            curr_height = heights[popped_idx]

            right_boundary = len(heights)
            left_boundary = stack[-1] if stack else -1
            curr_width = right_boundary - left_boundary - 1

            curr_area = curr_height * curr_width

            max_area = max(max_area, curr_area)

        return max_area

    # Day-07: 15/Aug/2026
    # Recognition Pattern: Every bar in the stack is waiting for its first smaller bar on the right.
    # Pattern: Stack (Monotonic)
    # Intuition:
        # Given bars of certtains heights and width=1
        # We need to find the max area of the rectangle
            # A rectangle is formed by 2 bars
        # We can use STACK to push the bars
        # Now for each bar who is currently the top of STACK, we can consider its next bar in the stack to be the exclusive LEFT boundary of the rectangle
        # NOw the task is to find a suitable exclusive RIGHT boundary.
        # Now for the curr top bar there are 2 options with which it can form a rectangle
            # O1: If the incoming bar height > height[stack[-1]]
                # the current top bar can still extend through this incoming bar, 
                # so its right boundary is still unknown  
                # just push the incoming bar.
            # O2: If the incoming bar height < height[stack[-1]]
                # It means for the current exclusive LEFT boundary we've found the exsclusive RIGHT boundary
                # Since the curr bar height is > the incoming bar , curr bar cant merge any further
                # So calculate curr_area and compute max_area
                    # curr_idx -> exclusive right boundary
                    # new stack top after pop -> exclusive left boundary
                    # width = right - left - 1
            # Bars remaining after traversal never found a smaller bar on the right,
            # so use len(heights) as their exclusive right boundary.        
        # TC = O(n), SC = O(n)
        # Mistakes Made:
            # The core intuition clicked this time, but the mental model was not correct
            # Eventually looked at prev notes and implementaion to get through
            # Last rating was 2.5/5, but this tiome i would rate 3/5 since the core intuition clicked right through
    def solve(self, heights: List[int]) -> int:
        bars = []
        max_area = float('-inf')

        for idx,height in enumerate(heights):
            # Current top bar encountered a smaller bar
            while bars and height < heights[bars[-1]]:
                popped_idx = bars.pop()
                curr_height = heights[popped_idx]

                right_boundary = idx
                left_boundary = bars[-1] if bars else -1
                curr_width = right_boundary - left_boundary - 1

                curr_area = curr_height * curr_width

                max_area = max(max_area, curr_area)
            
            bars.append(idx)

        # This is to handle the case, where the elements in the stack didnt encountered any smaller elemetrns to its right
        right_boundary = len(heights)
        while bars:
            popped_idx = bars.pop()
            curr_height = heights[popped_idx]

            left_boundary = bars[-1] if bars else -1
            curr_width = right_boundary - left_boundary - 1

            curr_area = curr_height * curr_width

            max_area = max(max_area, curr_area)

        return max_area

    
o = Solution()
# heights = [2,1,5,6,2,3]
heights = [7,1,7,2,2,4]

print(o.largestRectangleArea(heights))
