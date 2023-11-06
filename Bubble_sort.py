def Bubble_sort(arr):
    n = len(arr)
    for i in range(n): # for reducing the size of unsorted array at each pass 
        for j in range(0,n-1-i): # for comparing jth ele with j+1 element 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]                
    return arr

arr = [23,3,11,25,6,7,0]
result = Bubble_sort(arr)
print("array after sorted is:",result)


