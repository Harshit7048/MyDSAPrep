print("Second Problem , problem number 9")

# def check_Pallindrome(x):
#     s =str(x)

#     return s == s[::-1]

# print(check_Pallindrome(232))
# print(check_Pallindrome(656))
# print(check_Pallindrome(-131))

def check_pallindrome(x):
    if(x<0):
        return False
    if(x==0):
        return True
    if(x%10==0):
        return False

    original_x = x
    new_reversed = 0

    while x > 0:
        last_digit = x%10
        new_reversed = new_reversed * 10 + last_digit
        x = x // 10

    return original_x == new_reversed

print(check_pallindrome(1212133))