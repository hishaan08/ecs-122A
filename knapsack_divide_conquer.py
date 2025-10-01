#Knapsack with Divide and Conquer (Recursive)
#0/1 Knapsack using divide and conquer approach
def knapsack_dc(weights,values,capacity,n):
    if n==0 or capacity==0:
        return 0
    if weights[n-1]>capacity:
        return knapsack_dc(weights,values,capacity,n-1)
    return max(values[n-1]+knapsack_dc(weights,values,capacity-weights[n-1],n-1),
               knapsack_dc(weights,values,capacity,n-1))
#Example: weights=[10,20,30], values=[60,100,120], capacity=50, n=3
#Complexity: O(2^n) time, O(n) space
