# Encode and Decode Strings
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Machine 1 (sender) has the function:

# String encode(List<String> strs) {
#     // ... your code
#     return encoded_string;
# }
# Machine 2 (receiver) has the function:

# List<String> decode(String encoded_string) {
#     // ... your code
#     return decoded_strs;
# }
# So Machine 1 does:

# String encoded_string = encode(strs);
# and Machine 2 does:

# List<String> decoded_strs = decode(encoded_string);
# decoded_strs in Machine 2 should be the same as the input strs in Machine 1.

# Implement the encode and decode methods.

# Example 1:

# Input: strs = ["Hello","World"]

# Output: ["Hello","World"]
# Explanation:

# Solution solution = new Solution();
# String encoded_string = solution.encode(strs);

# // Machine 1 ---encoded_string---> Machine 2

# List<String> decoded_strs = solution.decode(encoded_string);

# Example 2:

# Input: strs = [""]

# Output: [""]

# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains any possible characters out of 256 valid ASCII characters.

# Follow up: Could you write a generalized algorithm to work on any possible set of characters?


class Solution:

    def encode1(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return '!'
        return '~'.join(strs)

    def decode1(self, s: str) -> List[str]:
        # print('s --> ', s)
        if s == '!':
            return []
        return s.split('~')
    

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)

        # print('res --> ', res)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        # print('s --> ', s)
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            # print('i, j, lenght --> ', i, j, length)
            word = s[j + 1 : j + 1 + length]

            res.append(word)

            i = j + 1 + length

        return res

o = Solution()
strs = ["Hello","World"]
encoded_str = o.encode(strs)
print(o.decode(encoded_str))