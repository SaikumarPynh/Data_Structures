def quicksort(arr,start,end):
    if start < end:
        pi = partition(arr,start,end)
        quicksort(arr,start,pi -1 )
        quicksort(arr,pi + 1,end)
    

def partition(arr,start,end):
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end:

        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end:
            arr[start],arr[end] = arr[end], arr[start]
    arr[end],arr[pivot_index]  = arr[pivot_index],arr[end]
        
    return end




arr = [4,2,7,66,3,22,5]
start = 0
end = len(arr) -1
quicksort(arr,start,end)
print("array after sorted is:",arr)