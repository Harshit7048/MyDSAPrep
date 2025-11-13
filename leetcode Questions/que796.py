# lets Do the Rotate String question

def rotate_string(s , goal):
    if (len(s) != len(goal)):
        return False
    cur_s = s
    n = len(cur_s)
    for i in range(0,n):
        if(cur_s == goal):
            return True
        cur_s = cur_s[-1]+cur_s[:-1]
    return False



print(rotate_string("abcde","bcdea"))


def check_place(s,goal):
    if(len(s) != len(goal)):
        return False
    double_s = s + s
    if(goal in double_s):
        return True
    else:
        return False

print(check_place("abcde","bcdea"))