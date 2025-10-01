#Binary Search (Divide and Conquer)
def binary_search(arr,target):
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
#Example: arr=[1,3,5,7,9,11,13], target=7
#Complexity: O(log n) time, O(1) space
