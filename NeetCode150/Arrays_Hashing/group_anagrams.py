# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

from collections import Counter, defaultdict

class Solution:
    # Brute Force : O(n x m) + O(n X (n x m)) => O(n^2 x m), where n : len of strs and m : len of strs ele
    def groupAnagrams_1(self, strs: List[str]) -> List[List[str]]:
        strs_counters = []
        for str in strs:
            strs_counters.append(Counter(str))

        print(strs_counters)

        res = []

        for idx_1 in range(len(strs_counters)):
            if strs_counters[idx_1] != -1:
                curr_res = [strs[idx_1]]
                for idx_2 in range(idx_1+1, len(strs_counters)):
                    if strs_counters[idx_2] != -1 and strs_counters[idx_1] == strs_counters[idx_2]:
                        curr_res.append(strs[idx_2])
                        strs_counters[idx_2] = -1
                res.append(curr_res)

        return res
    
    # Frozen Set : O(n x m), where n : len of strs and m : len of strs ele
    def groupAnagrams_2(self, strs: List[str]) -> List[List[str]]:
        strs_counters_map = dict()
        for str in strs:
            curr = frozenset(Counter(str).items())
            if curr in strs_counters_map:
                strs_counters_map[curr].append(str)
            else:
                strs_counters_map[curr] = [str]

        # print('strs_counters_map --> ', strs_counters_map)
        res = []

        for grp in strs_counters_map.values():
            res.append(grp)

        return res
    

    # Frozen Set : O(n x m), where n : len of strs and m : len of strs ele
    # Better pythonic code
    def groupAnagrams_3(self, strs: List[str]) -> List[List[str]]:
        # Automatically initializes a new list if a key doesn't exist
        strs_counters_map = defaultdict(list)

        for string in strs:
            curr = frozenset(Counter(string).items())
            strs_counters_map[curr].append(string)


        return list(strs_counters_map.values())
    
    # Use 26 freq count array
    def groupAnagrams4(self, strs: List[str]) -> List[List[str]]:
        strs_counters_map = defaultdict(list)

        for string in strs:
            cnt_array = [0]*26
            
            for char in string:
                cnt_array[ord(char) - ord('a')] += 1

            strs_counters_map[tuple(cnt_array)].append(string)
        # print(strs_counters_map)
        return list(strs_counters_map.values())
        

    # Day-1: 18/June/2026
    # Pattern: Cannonical Pattern -> Map of Maps/26-char map
    # Recognition Trigger: Check for the char freqs and compare them. 
    # Brute Force: Two loops. O(n2)
    # Optimization Insight: Can use a Counter/Map of Maps
    def groupAnagrams5(self, strs: List[str]) -> List[List[str]]:
        strs_cntr = [frozenset(Counter(string).items()) for string in strs]
        res = defaultdict(list)

        for idx in range(len(strs)):
            res[strs_cntr[idx]].append(strs[idx])

        return list(res.values())
    

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            curr = [0] * 26
            for char in string:
                curr[ord(char)-ord('a')] +=1

            res[tuple(curr)].append(string)

        return list(res.values())

o = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]

print(o.groupAnagrams(strs))
