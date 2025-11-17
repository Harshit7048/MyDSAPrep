# Recursion , where we call a function inside its own scope
# let's see a example
 
print("hello")
s =0
def greet():
    global s
    if(s==4):
        return
    print("hello")
    s += 1
    greet()

# greet()

# let's see another example of recursion with use of parameters

def greet_again(x,n):
    if(n==0):
        return
    print(x)
    greet_again(x,n-1)

# greet_again(15,4) 

#  there both code are the examples of the recursion

# let's do another example of using parameters

def val(i,n):
    if(i>n):
        return
    print(i)
    val(i+1,n)

# val(1,8)

#  above is a head recursion where job is getting done forst then we are calling function 

# let's see the  Tail recursion also know as backtracking 
# this will print out value in backward

def back(i,n):
    if(i>n):
        return
    back(i+1,n)
    print(i)

# back(1,8)

# see the output is in backward


#  printing 1 to N using tail 

def func(n):
    if(n==0):
        return
    func(n-1)
    print(n)

func(10)

