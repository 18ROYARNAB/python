# RIGHT ROATATE ANY ARRAY BY 1 PLACE

def rightRoatae(arr,k):
    n=len(arr)
    for j in range (0,k,1): 
        temp=arr[-1]
        for i in range (n-2,-1,-1):
            arr[i+1]=arr[i]
        arr[0]=temp
    return arr

num=[10,232,3,2,22,1,32,90]
print(rightRoatae(num,3))