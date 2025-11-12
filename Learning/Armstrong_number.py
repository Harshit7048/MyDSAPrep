print("armstrong Number")

def check_arm_strong_num(n):
    nod = len(str(n))
    total=0
     
    num = n
    while num>0:
        last_d = num %10
        total += last_d**nod
        num = num//10
    
    return  total == n


print(check_arm_strong_num(1534))

# here we had written the code for our armstrong number , we used the pallindrome thing also