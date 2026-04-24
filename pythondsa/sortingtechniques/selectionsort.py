def selectionSort(arr : list):
    for i in range (len(arr)):
        min_idx=i
        for j in range (i+1,len(arr)):
            if arr[min_idx]>arr[j]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr
array=[32,435,45,6,565,3,2]
print(f"Sorted array : {selectionSort(array)}")