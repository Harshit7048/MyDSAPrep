# Let's see the bubble sort

# def bubbleSort(nums):
#     for i in range(0,len(nums)-1):
        
#         for j in range(i+1,len(nums)-1):
#             if (nums[i]>nums[j]):
#                 nums[i],nums[j]=nums[j],nums[i]
    
#     return nums

#  So the above code is my thinking , and it is not a good code , It is just a diffrent version of selection sort not a bubble sort as , bubble sort check adjacent elements and in the above code we are checking the every element with first one 

def bubble_sort_2(nums):
    n=len(nums)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if(nums[j]>nums[j+1]):
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums

# This one is real bubble sort as it compares adjacent elements


# print(bubbleSort([5,4,7,4,9,3,9]))
print(bubble_sort_2([7,8,3,9,2,8,4,8]))