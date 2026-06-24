# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution:
    # BruteForce:
    # 1. Sort the array => [1,2,3,4,100,200 => O(nlogn)
    # 2. Use 2 loops to find the max consecutive sequence => O(n2)
    # 3. TC = O(n2)

    # Optimised Approach:
    # 1. Create a bucket_arr of size max(nums)+1 with 0 and 1 elements marking 0 as absence and 1 as presence of element 
    # ==> [100,4,200,1,3,2] 
    # idx : 0 1 2 3 4 5 6 7 .......99 100 101 .... 199 200 
    # <==> [0,1,1,1,1,0,0,0 .......,0, 1,  0, ...., 0,   1]
    # THE ABOVE WILL WORK ONLY IF THERE ARE POSITIVE ELEMENTS IN INPUT ARR
    # Modified Approach:
    # Get the min_ele and max_ele of nums 
    # Iterate from min_ele -> max_ele and check whether the curr ele is in nums_set 
    # TC = O(R), R = range(min, max) => O(2n)

    class Solution:
        def longestConsecutive1(self, nums: List[int]) -> int:
            if len(nums) == 0:
                return 0
            
            nums_set = set(nums)
            min_ele, max_ele = min(nums), max(nums)
            res = float('-inf')
                        
            i = min_ele
            while i <= max_ele:
                if i not in nums_set:
                    i += 1
                else:
                    curr_res = 1
                    j = i+1

                    while j <= max_ele and j in nums_set:
                        curr_res += 1
                        j += 1

                    i = j
                    res = max(res, curr_res)

            return res

        # Optimised Approach : 
        # A consecutive sequence must have a start element 
        # ==> curr_ele can be said to be the starting element of the sequence iff (curr_ele - 1) doesnt exist in the set
        # ==> Once the starting element is identified we can walk down the sequence by incrementing the (curr_ele + 1) and checking its exisstence in set
        # TC = O(n)
        def longestConsecutive2(self, nums: List[int]) -> int:
            res = 0
            nums_set = set(nums)

            for ele in nums_set:
                # Chck whether the curr ele , can be the starting point of the consecutive sequence
                if ele-1 not in nums_set:
                    curr_len = 1

                    next_ele = ele+1
                    while next_ele in nums_set:
                        curr_len += 1
                        next_ele += 1

                    res = max(res, curr_len)

            return res


        # Day-7 : 24/June/2026
        # Pattern: Set
        # Trigger : For any element ot be the start of the seq, (ele-1) should not exists
        # Note: Was able to solve
        def longestConsecutive(self, nums: List[int]) -> int:
            if len(nums) == 0:
                return 0
            nums_set = set(nums)
            res = 1

            for num in nums_set:
                if num-1 not in nums_set:
                    curr_seq = 1
                    next_num = num+1

                    while next_num in nums_set:
                        curr_seq += 1
                        next_num += 1

                    res = max(res, curr_seq)

            return res
        
    o = Solution()
    # nums = [100,4,200,1,3,2]
    # nums = [0,3,7,2,5,8,4,6,0,1]
    # nums = [1,0,1,2]
    nums = []
    print(o.longestConsecutive(nums))
