#0/1 Knapsack (bottom-up DP)
#items: list of (weight,value), W: capacity
def knapsack_01(items,W):
    n=len(items)
    dp=[[0]*(W+1) for _ in range(n+1)]
    for i in range(1,n+1):
        w,v=items[i-1]
        for cap in range(W+1):
            dp[i][cap]=dp[i-1][cap]
            if cap>=w:
                dp[i][cap]=max(dp[i][cap],dp[i-1][cap-w]+v)
    return dp[n][W]
#Complexity: O(n*W) time, O(n*W) space (can be optimized to O(W))