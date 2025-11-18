#  Let's finally go through the sorting algorithms , 
# First lets see the selction sort

def selection_sort(arr):
    n=len(arr)

    for i in range(0,n):
        min_idx = i
        for j in range(i+1,n):
            if(arr[j]<arr[min_idx]):
                min_idx=j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    
    return arr

print(selection_sort([3,4,8,9,6,5,9,4]))

# Time complexity for this is -> O(n(n-1)/2) - O(N^2)