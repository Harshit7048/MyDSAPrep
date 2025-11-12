from math import sqrt

print("Printing all the factors of a given number") 

# def Factors(n):
#     print(n)
#     num = 1
#     list_Factors=[]
#     for i in range(1,n+1):
#         num_fact = i
#         if(n%i==0):
#             list_Factors.append(num_fact)
        
#     return list_Factors


# print(Factors(15))
# print(Factors(20))

# lets write a more optimised solution 

# def factors(n):
#     result =[]
#     for i in range(1,n//2 +1):
#         if(n%i==0):
#             result.append(i)
#     result.append(n)

#     return result

# print(factors(25))
# print(factors(75))
# print(factors(10))

# Final optimal solution

def factor(n):
    result=[]

    for i in range(1, int(sqrt(n))+1):
        if(n%i==0):
            result.append(i)
            if(n//i != i):
                result.append(n//i)
    result.sort()

    return result

print(factor(70))
