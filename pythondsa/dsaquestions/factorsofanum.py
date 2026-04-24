#BRUTE FORCE APPROACH 
def factor_Nums(num):
    result=[]
    for i in range(1,num+1):
        if 0==num%i:
            result.append(i)
    return result

#better approach
def better_factor(num):
    result=[]
    for i in range(1,num//2):
        if num%i==0 : 
            result.append(i)
    result.append(num)
    return result

#optimal approach 
import math
def optimal_factor(num):
    result=[]
    for i in range(1,int(math.sqrt(num)+1)):
        if num%i==0:
            result.append(i)
            if num//i != i:
                result.append(num//i)
    return result


print(factor_Nums(36))
    