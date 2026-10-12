
def min_coins_for_change(coins, amount):
    # Initialize DP table
    dp = [amount + 1] * (amount + 1)

    # Base case: 0 coins are needed for amount 0
    dp[0] = 0

    # Calculate minimum coins for each amount
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return -1 if the amount cannot be formed
    return dp[amount] if dp[amount] <= amount else -1


# Example 1: Standard coin system
coins1 = [1, 2, 5]
amount1 = 11
print("Minimum coins for", amount1, ":", 
      min_coins_for_change(coins1, amount1))

# Example 2: Greedy approach would not always be optimal
coins2 = [1, 3, 4]
amount2 = 6
print("Minimum coins for", amount2, ":", 
      min_coins_for_change(coins2, amount2))

# Example 3: Impossible configuration
coins3 = [2]
amount3 = 3
print("Minimum coins for", amount3, ":", 
      min_coins_for_change(coins3, amount3))
print(92460118292)
