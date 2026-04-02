n=int(input("enter num"))
num=n
while num>0:
    last_digit=num%10
    print(last_digit)
    num //=10