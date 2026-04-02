n=int(input("enter num"))
num=n
new=0
while num>0: 
    new+=num%10
    new*=10
    num//=10
print(new)