# def insertionsort(arr):
#     for i in range(1,len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0  and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr

# #driver code
# arr = [75,90,60,85]
# result = insertionsort(arr)
# print("the array after the sorted is:",result)
def InsertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        j = i-1
        while(j >=0):
            if arr[j+1] < arr[j]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
            j -= 1
    return arr
a = [3,2,5,7,1,0]
c = InsertionSort(a)
c