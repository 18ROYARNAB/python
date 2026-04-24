def reverse_Arr(num : list, left : int , right : int )-> list :
    if left>=right:
        return num
    num[left],num[right]=num[right], num[left]
    return reverse_Arr(num,left+1,right-1)

num=[32,3212,94,49,47,261]
left=0
right=len(num)-1
reversedarray : list =reverse_Arr(num,left,right)
print(reversedarray)