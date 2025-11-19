# Let's Now look the Insertion Sort And see how it works
print("hello 1")
def inser_sort(nums):
    n = len(nums)
    for i in range(1,n):
        key=nums[i]
        j = i-1
        while j>=0 and nums[j]>key:
            nums[j +1] = nums[j]
            j-= 1
        nums[j+1]=key
    return nums

print(inser_sort([2,5,6,4,7,8,5,9,10,1]))

# Time complexity O(n(n+1)/2) -> o(n^2)