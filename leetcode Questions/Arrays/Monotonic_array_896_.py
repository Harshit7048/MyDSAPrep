print("monotonic array check")

# def isMonotonic(nums):
#     n=len(nums)
#     monotone_increas = False
#     monotone_decrease = False

#     for i in range(0,n-1):
#         idx_i = i
#         for j in range(idx_i , n-1):
#             if(i<=j):
#                 if(nums[i]<=nums[j]):
#                     monotone_increas = True
#                 else:
#                     monotone_increas = False
#     return monotone_increas
    
def isMonotonic(nums):
    # if nums[-1] - nums[0] < 0:
    #     nums.reverse()
    increase = True
    decrease = True
    for i in range(0,len(nums)-1):
        if not (nums[i]<= nums[i+1]):
            increase = False
        if not (nums[i]>=nums[i+1]):decrease = False
    return increase or decrease

print(isMonotonic([1,2,2,3,9,2]))
print(isMonotonic([1,3,3,4,5,8,2,2]))
