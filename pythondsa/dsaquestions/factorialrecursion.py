def fact(n):
    if 1==n:
        return 1
    return n*fact(n-1)

a=fact(5)
print(a)
