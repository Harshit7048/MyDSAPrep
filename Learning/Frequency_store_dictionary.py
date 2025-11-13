# Storing frequency in dictionary of an array

def freq_map(inp):
    frequency_map = {}
    for i in range(0,len(inp)):
        if(inp[i] in frequency_map):
            frequency_map[inp[i]] += 1
        else:
            frequency_map[inp[i]] = 1
    print(frequency_map)

freq_map([1,1,1,5,5,5,6])

# Another method

def hash(nums):
    hash_map = {}
    for i in range(0,len(nums)):
        hash_map[nums[i]] = hash_map.get(nums[i],0)+1
    return hash_map

print(hash([1,1,3,3,4,4,4,4,5]))