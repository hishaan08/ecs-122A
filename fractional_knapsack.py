#Fractional Knapsack (Greedy)
#Maximize value with fractional items allowed
def fractional_knapsack(weights,values,capacity):
    n=len(weights)
    items=list(zip(weights,values))
    items.sort(key=lambda x:x[1]/x[0],reverse=True)
    total_value=0
    for weight,value in items:
        if capacity>=weight:
            total_value+=value
            capacity-=weight
        else:
            total_value+=value*(capacity/weight)
            break
    return total_value
#Example: weights=[10,20,30], values=[60,100,120], capacity=50
#Complexity: O(n log n) time, O(1) space
