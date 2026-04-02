i=0
while i<=10:
    print("roy",i)
    i+=1


# numbers from loop

lsit1=[1,4,5,7,6,4,3,4,3,43,5,56,67,5675,6534,54]
for i  in range(len(lsit1)):
    print(lsit1[i])

#searchingg in tuple using loop
tup1=(1,2,34,5,56,45,54,56,675,984)
target = int(input("entr to searcch"))
for i in range (len(tup1)):
    if target==tup1[i]:
        print("Element found at index : ",i)
