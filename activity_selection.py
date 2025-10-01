#Activity Selection Problem (Greedy)
#Select maximum number of non-overlapping activities
def activity_selection(start,end):
    n=len(start)
    activities=list(zip(start,end,range(n)))
    activities.sort(key=lambda x:x[1])
    selected=[]
    last_end=0
    for start_time,end_time,index in activities:
        if start_time>=last_end:
            selected.append(index)
            last_end=end_time
    return selected
#Example: start=[1,3,0,5,8,5], end=[2,4,6,7,9,9]
#Complexity: O(n log n) time, O(n) space
