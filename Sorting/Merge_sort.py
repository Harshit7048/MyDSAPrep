# Let's see the MERGE SORT this is one of the important sorting algorithm as it have different time complexity then the other sorting methods

def merge_array(left , right):
    results=[]
    i,j=0,0
    n,m=len(left),len(right)

    while i<n and j<m:
        if(left[i]<right[j]):
            results.append(left[i])
            i +=1
        else:
            results.append(right[j])
            j+=1
    if(i<n):
        while i<n:
            results.append(left[i])
            i+=1
    if(j<m):
        while j<m:
            results.append(right[j])
            j+=1
    return results

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    n = len(arr)
    mid=n//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge_array(left,right)

print(merge_sort([1,5,8,3,9,2,7,6,4,9]))
# Time complexity -> O(NlogN)
# Space complexity -> O(N)
    


