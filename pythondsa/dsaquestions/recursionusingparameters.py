# PRINT X,  N TIMES USINF RECUSRION
def func(x,n):
    if 0==n:
        return
    print(x)
    func(x,n-1)
func(15,4)

# PRINT 1 TO N USING RECURSION

def func1(i,n):
    if i==n+1:
        return
    print(i)
    func1(i+1,n)
func1(1,5)

# print n to 1 using tail recusrion or backtracking
def func1(i,n):
    if i==n+1:
        return
    func1(i+1,n)
    print(i)
    
func1(1,5)
