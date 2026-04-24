def insertionSort( arr : list ):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            key=arr[i+1]
            j=i+1
            while j!=0:
               if key<arr[j]:
                   