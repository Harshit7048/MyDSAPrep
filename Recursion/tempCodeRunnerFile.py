f rec_str(s):
     n=len(s)
     l=0
     r=n-1
     if(s[l] != s[r]):return False

     rec_str(s,l+1,r-1)

print(rec_str("mom"))
     