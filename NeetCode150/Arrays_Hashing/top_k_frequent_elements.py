# 347. Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2

# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1

# Output: [1]

# Example 3:

# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

# Output: [1,2]

 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

from collections import Counter
class Solution:
    def topKFrequent_1(self, nums: List[str], k : int) -> List[int]:
        cntr = Counter(nums)
        print(cntr)
        freq_sorted = sorted(cntr.items(), key=lambda x:x[1], reverse=True)
        print(freq_sorted)
        
        res = []
        ptr = 0
        while ptr < k:
            res.append(freq_sorted[ptr][0])
            ptr +=1

        return res
    

    def topKFrequent2(self, nums: List[str], k : int) -> List[int]:
        cntr = Counter(nums)
        print(cntr)
        
        bucket_array = [[] for i in range(len(nums)+1)]

        for num, freq in cntr.items():
            bucket_array[freq].append(num)

        print('bucket_array --> ', bucket_array)

        res = []
        ptr = 0
        for idx in range(len(bucket_array)-1, 0, -1):
            for num in bucket_array[idx]:
                if ptr < k:
                    res.append(num)
                    ptr +=1
                else:
                    break

        return res


    # Day-1: 18/June/2026
    # Pattern: K-Map/ Bucket Sort
    # Recognition Trigger: Freq range is bounded by the size of input array
    # Brute Force: Two loops. O(n2)
    # Optimization Insight: Create a freq array of size len(nums)
    def topKFrequent3(self, nums: List[str], k : int) -> List[int]:
        res = []
        freq_arr = [[] for idx in range(len(nums)+1)]
        freq_map = Counter(nums)

        for ele, freq in freq_map.items():
            freq_arr[freq].append(ele)
        
        for idx in range(len(nums), -1, -1):
            curr = freq_arr[idx]
            if k:
                for idx1 in range(len(curr)):
                    res.append(curr[idx1])
                    k -=1
            else:
                return res

    # Day-7: 24/June/2026
    # Pattern: Bucket Sort
    # Note: Was able to solve
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        nums_freq = Counter(nums)

        bucket_freq_arr = [[] for i in range(len(nums)+1)]

        for num, freq in nums_freq.items():
            bucket_freq_arr[freq].append(num)

        # print('bucket_freq_arr --> ', bucket_freq_arr)
   
        for idx1 in range(len(bucket_freq_arr)-1, -1, -1):
            for idx2 in range(len(bucket_freq_arr[idx1])):
                if k:
                    res.append(bucket_freq_arr[idx1][idx2])
                    k -=1
                else:
                    return res
                    
        return res

    # Day-30: 21/July/2026
    # Recognition Trigger: 
        # Need Top K based on frequency/ranking.
        #           ↓
        # Count frequencies first.
        #           ↓
        # Then think:
        #  Bucket Sort (if frequency is bounded)
        #  Heap (if K is small)
    # Pattern: Bucket Sort + Hash Map or Heap
    # Intuition:
        # Since we need TOP K FREQUENT elemnts
        # First thought was to sort the arr and scrap the top K , but this will lead to TC:O(nlogn)
        # Inorder to optimise it, we can think of using a cnt_array
        # The lenght of cnt_array can be max len(nums)+1, since in any given array the max frequency would be len(nums), given the arr contains only 1 unique element
    # TC = O(n), SC = O(n+n)
    # Mistakes Made:
        # None
    def solve(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq_map = Counter(nums)
        cnt_arr = [[] for _ in range(len(nums)+1)]

        for num, freq in freq_map.items():
            cnt_arr[freq].append(num)

        ptr = len(nums)
        while k > 0 and ptr >= 0:
            for num in cnt_arr[ptr]:
                res.append(num)
                k -= 1
            ptr -= 1
        return res

o = Solution()
nums = [1]
k = 1

print(o.topKFrequent(nums, k))
