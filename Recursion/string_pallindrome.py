# Lets check if a string is pallindrome or not

# let's first do it with recursion

def str_pallindrome(s):
     l=0
     r=len(s)-1
     while l<r:
          if(s[l] != s[r]):
               return False
          l +=1
          r -=1
     return True

print(str_pallindrome("abcddcbas"))


def rec_str(s,l,r):
     if(l>r): return True
     if(s[l] != s[r]):return False

     return rec_str(s,l+1,r-1)

def ispallindrome(s):
     return rec_str(s,0,len(s)-1)

print(ispallindrome("abcddcba"))
     