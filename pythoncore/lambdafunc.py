#  lambda function
nums=[10,11,23,20,30,44,49,50]

def even(x):
    if x%2==0:
        return x

s=list(filter(even,nums))
print(s)

eveen=list(filter(lambda x: x%2 ==0,nums))
print(eveen) 
