# Reverse an array usiing recursion

def reverse(arr,left , right):
    if(left>=right):
        return arr
    arr[left] ,arr[right] = arr[right] , arr[left]
    
    reverse(arr,left+1,right-1)
    return arr

print(reverse([1,2,5,8,7,6,9,8,3],2,6))
    