import math

def factorial(n):
    ans = 1
    for i in range(1,n+1):
        ans = ans*i
    return ans

def mysin(x):
    return sum([(-1)**k*(x**(2*k+1))/factorial(2*k+1) for k in range(1,20)]) + x

a = 30
X = math.pi*a/180

print(mysin(X))
print(math.sin(X))