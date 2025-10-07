print("Question 3 , remove duplicate element from sorted array")

def removeDuplicate(self,nums):
    k=1
    for i in range(0 ,len(nums)):
        if(nums[i] != nums[i-1]):
            k += 1
    
    currentIndex=1
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[currentIndex] = nums[i]
            currentIndex += 1
    
    for i in range(currentIndex,len(nums)):
        nums[i]="_"
    return k

print(removeDuplicate([3,3,3,4,5,5,5,6,7,7,8,9]))