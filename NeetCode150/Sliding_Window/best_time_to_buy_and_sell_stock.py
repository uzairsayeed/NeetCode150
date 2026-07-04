# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

# | Window Type   | Template                                                |
# | ------------- | ------------------------------------------------------- |
# | Variable Size | Expand → While Invalid: Shrink → Update                 |
# | Fixed Size    | Expand → If Window Size == K: Update (if valid) → Slide |

class Solution:
    # BF: For every price find the max profit and calculate overall profit
    # TC = O(n2)
    def maxProfit1(self, prices: List[int]) -> int:
        res = 0
        
        for buy in range(len(prices)):
            curr_profit = 0
            for sell in range(buy+1, len(prices)):
                if prices[buy] < prices[sell]:
                    curr_profit = max(curr_profit, prices[sell]-prices[buy])
            res = max(curr_profit, res)

        return res

    # Approach-1: Suffix Maximum (Right-to-Left Scan)
    # Scan from right to left while maintaining the maximum selling price available in the future. 
    # For each day, I compute the profit if I bought on that day and sold at the best future price.
    # Pattern: Greedy / Running Extreme (Suffix Maximum)
    # Recognition Trigger: Max profit means max_Sell_price and min_buy_price. 
    # Im travelling from right -> left , if i encounter current element at 'i' > max_right(right ptr) then ill update my right ptr to current. AS i want to max profit ==> max_right_price.
    # and for every cuurent ele at 'i' if its value is < max_right , Ill calculate profit while maintaining global maxima
    # TC = O(n), SC = O(1)

    # NOTE: This problem has two equally valid mental models:
    # | Direction    | Maintained Value     | Question Being Answered                    |
    # | ------------ | -------------------- | ------------------------------------------ |
    # | Left → Right | Minimum price so far | "If I sell today, what's the best profit?" |
    # | Right → Left | Maximum price ahead  | "If I buy today, what's the best profit?"  |

    def maxProfit2(self, prices: List[int]) -> int:
        res = 0
        left, right = len(prices)-2, len(prices)-1

        while left >= 0:
            if prices[right] < prices[left]:
                right = left
                left -= 1
            else:
                res = max(res, prices[right]-prices[left])
                left -= 1

        return res
    
    # Standard Approach:
    # Find max(prices[j]-prices[i]), whre j > i | i = buying day , j = selling day
    # Now for every 'j' ==> What's the best day before today to buy ? Its the one with least value
    # So if we maintain min_price_seen_so_far for evry 'j' we can maximise the profit. Since max profit = J value - least i value.
    def maxProfit3(self, prices: List[int]) -> int:
        res = 0
        i, j = 0, 1
        min_price = prices[0]

        while j < len(prices):
            if prices[j] > prices[i]:
                res = max(res, prices[j]-min_price)
            else:
                min_price = prices[j]
                i = j
            j += 1

        return res
    

    # Pattern: Running Minimum (Prefix Minimum)
    # Recognition Trigger:
    # Need to maximize (arr[j] - arr[i]) where j > i.
    # Core Insight:
    # For every position j, the best i is simply the minimum value seen before j.
    # Maintain:
    # 1. min_price_so_far
    # 2. max_profit_so_far
    # For each element:
    # - Compute profit if sold today.
    # - Update global maximum profit.
    # - Update running minimum.
    def maxProfit4(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            # Sell today using the cheapest buy seen so far
            max_profit = max(max_profit, price - min_price)

            # Update cheapest buy opportunity
            min_price = min(min_price, price)

        return max_profit

    # Day-1: 26-Jun-2026

    # Pattern:
    # Running Minimum (Prefix Minimum)

    # Recognition Trigger:
    # Need to maximize (prices[j] - prices[i]) where j > i.

    # Core Insight:
    # Treat every current day as the selling day.
    # To maximize profit, the buying day should be the minimum stock price seen before today.

    # Maintain:
    # 1. min_price_so_far
    # 2. max_profit_so_far

    # Invariant:
    # Before processing each day,
    # min_price stores the minimum stock price seen so far.

    # Algorithm:
    # 1. Calculate profit if sold today.
    # 2. Update global maximum profit.
    # 3. Update minimum stock price.

    # TC: O(n)
    # SC: O(1)
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            max_profit = max(max_profit, price-min_price)
            min_price = min(min_price, price)
        return max_profit
    

    # Day-07: 03/July/2026
    # Notes: I was able to figure out the intuition => (For current 'i' cosnider it as the selling day and minus the min price seen so far[left_min])
    # Did 2 mistakes though
    # 1. Was calculating 'min_price_seen' first then 'curr_profit' => It should be the other way, since we want to minis the min price seen so far not including the curr price
    # 2. USed 'min(min_price_seen, prices[idx-1])' => the correct is to include the current price inorder to calculate the next min price seen so far.
    def solve(self, prices: list[int]) -> int:
        res = 0
        min_price_seen = prices[0]

        for idx in range(1,len(prices)):
            curr_profit = prices[idx] - min_price_seen
            min_price_seen = min(min_price_seen, prices[idx])
            res = max(res, curr_profit)
        return res
o = Solution()
prices = [7,6,4,3,1]
# prices = [7,1,5,3,6,4] 
# prices = [2,4,1]
# prices = [3,2,6,5,0,3]

print(o.maxProfit(prices))
