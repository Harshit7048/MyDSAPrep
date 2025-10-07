print("Second Problem , problem number 9")

def check_Pallindrome(x):
    
    str1 = str(x)
    
    arr = list(str1)
    print(arr)
    for i in range(0,len(arr)):
        if(arr[i]=="2"):
            print("this is pallindrome")
    return x

print(check_Pallindrome(232))