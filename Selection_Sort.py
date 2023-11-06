def Selection_Sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index] 
    return arr
arr = [34,2,66,9,6,1]
result = Selection_Sort(arr)
print("array after sorting is:",result)