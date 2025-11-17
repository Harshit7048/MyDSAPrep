# let's see the Parameterized and functional Recursion








# Functional Recusrion

def add(n):
    if(n==1):
        return 2
    return n + add(n-1)

print(add(97))

#  So this is an funtional recursion where we are actually returning something , not just printing , This will help in future 


#  let's write a code for factorial of a number n

def fact(n):
    if(n==1):
        return 1
    return n * fact(n-1)

print(fact(10))

# Time complexity - O(N)