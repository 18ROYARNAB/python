# 1 to n sum in functonal recursion we return function no print an all
def func(n):
    if n == 1:
        return 1
    return n+func(n-1)

sum=func(5)
print(sum)

def func1(sum,i,n):
    if i>n:
        print(sum)
        return 
    func1(sum+i,i+1,n)
    print(i)

func1(0,1,5)
