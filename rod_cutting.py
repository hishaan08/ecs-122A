#Rod Cutting Problem (Dynamic Programming)
#Given rod of length n and prices for each length, find max value
def rod_cutting(prices,n):
    dp=[0]*(n+1)
    for i in range(1,n+1):
        for j in range(1,i+1):
            dp[i]=max(dp[i],prices[j-1]+dp[i-j])
    return dp[n]
#Example: prices=[1,5,8,9,10,17,17,20], n=8
#Complexity: O(n^2) time, O(n) space
