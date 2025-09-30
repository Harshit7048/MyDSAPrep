print("First problem")

# what I had wrote here is a brute force mehod , which I had think at first I saw the problem , but it have a better solution in O(N)
# 
# 
# 
# arr = [1,3,5,6,9]
# target = 7

# for i in arr:
#     for j in arr:
#         if(i+j==target):
#             print("found")
            
#     else:
#         continue

arr=[1,3,4,5,6,9]
tar = 13


def twoSum(arr,tar):
    target = tar
    hash_map ={}
    num = len(arr)
    for i in range (0,num):
      remaining = target - arr[i]
      if(remaining in hash_map):
       return [hash_map[remaining],i]
      hash_map[arr[i]] = i

print(twoSum(arr,tar))