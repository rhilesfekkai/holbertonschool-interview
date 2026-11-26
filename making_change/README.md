# Making Change

Calculate the fewest number of coins needed to meet a given amount.

## Function

makeChange(coins, total)

Returns the minimum number of coins needed, or -1
if the amount cannot be met.

## Algorithm

Dynamic Programming (Bottom-Up).

Time complexity: O(total * len(coins))
Space complexity: O(total)
