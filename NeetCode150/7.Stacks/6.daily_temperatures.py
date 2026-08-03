# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

class Solution:
    # Day-0: 03/Aug/2026
    # Recognition Pattern: For every element, find the first greater element to its right and calculate the distance to it.
    # Pattern: Monotonic Stack
    # Intuition:
        # Every element in satck is waiting for a higher element
        # which is nothing but every temp in strack is waiting for a warmer temp 
    # Mistakes Made:
        # None
    # TC = O(n)
    # SC = O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warm_records = []
        res = [0] * len(temperatures)

        for idx,temp in enumerate(temperatures):
            while warm_records and temperatures[warm_records[-1]] < temp:
                popped_idx = warm_records.pop()
                res[popped_idx] = idx - popped_idx

            warm_records.append(idx)

        return res

o = Solution()
# temperatures = [73,74,75,71,69,72,76,73]
# temperatures = [30,40,50,60]
temperatures = [30,60,90]
print(o.dailyTemperatures(temperatures))


            
