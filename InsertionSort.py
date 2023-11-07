def insertionsort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0  and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#driver code
arr = [75,90,60,85]
result = insertionsort(arr)
print("the array after the sorted is:",result)
