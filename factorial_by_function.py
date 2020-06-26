def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
def f():
    x = int(input("Enter the number to find factorial: "))
    print("\n Factorial of",x,"is",fact(x))
    
def fac(a):
    p = 1
    for i in range(1,a+1):
        p *= i
    print("\n Factorial of",a,"is",p)
   
def n():
    b = int(input("Enter the number to find factorial: "))
    fac(b)
    
f()
n()