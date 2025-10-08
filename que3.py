# print("Question 3 , remove duplicate element from sorted array")
def removeDuplicates(nums):
     n = len(nums)
     if(n==1): return 1

     i=0
     j=1
     while j<n:
        if nums[j] != nums[i]:
            i += 1
            nums[i],nums[j]=nums[j],nums[i]
        j += 1
     return i+1

print(removeDuplicates([3,3,3,4,5,5,5,6,7,7,8,9,9]))