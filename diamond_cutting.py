#Diamond Cutting Problem (Dynamic Programming)
#Cut diamond into pieces to maximize value
def diamond_cutting(weights,values,capacity):
    n=len(weights)
    dp=[[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(capacity+1):
            dp[i][w]=dp[i-1][w]
            if weights[i-1]<=w:
                dp[i][w]=max(dp[i][w],dp[i-1][w-weights[i-1]]+values[i-1])
    return dp[n][capacity]
#Example: weights=[1,3,4,5], values=[1,4,5,7], capacity=7
#Complexity: O(n*W) time, O(n*W) space
