def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w: 
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
            else:  # If the item cannot be included
                dp[i][w] = dp[i-1][w] 
    return dp[n][capacity]
weights = [2, 4, 3, 6]
values = [3, 7, 7, 3]
capacity = 8
print(f"Maximum value that can be obtained: {knapsack(weights, values, capacity)}")
