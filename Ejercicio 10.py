def factorial(n):
    if n == 0 or n == 1:
        resultado = 1
    elif n>1:
        f = 1
        for i in range(1,n+1):
            f*=i
    return f

x = 10
print(factorial(x))



