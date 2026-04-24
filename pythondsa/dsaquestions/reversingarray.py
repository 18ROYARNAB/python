#swipping by 2 pointer left and right rreversing the array and can be used to revert any particular index in array
def rever(arr : list,left:int,right:int):
    if left>=right:
        return arr
    # Swipe both left and right index
    arr[left],arr[right]=arr[right],arr[left]
    return rever(arr,left+1,right-1)
    
import numpy as np
list=np.random.randint(1,100,size=10).tolist()
print(list)
reversed=rever(list,0,len(list)-1)
print(reversed)