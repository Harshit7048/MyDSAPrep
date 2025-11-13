# Let's look for what is hashing and how it works

def print_itration(n ,m):
    hash_list = [0] * len(n)
    for nums in n:
        hash_list[nums] += 1
    
    for nums in m:
        if( nums<0 or nums>11):
            print(0)
        else:
            print(hash_list[nums])

print_itration([1,3,4,5,5,6,6,6,7,7,7,8] , [2,4,5,5,6,7,7,7,8])