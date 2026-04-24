def fib(n : int):
    if 0==n:
        return 0
    if 1==n:
        return 1
    return fib(n-1)+fib(n-2)


b=fib(5)
for i in range (0,6):
    print (fib(i))