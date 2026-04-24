def palindrome(str1:str,left,right):
    while left<right:
        if str1[left]!=str1[right]:
            return False
        left += 1 
        right-= 1
    return True

str1=input("enter to check palindrome or not :")
left=0
right=len(str1)-1
print(f" String is Palindrome : ",palindrome(str1,left,right))