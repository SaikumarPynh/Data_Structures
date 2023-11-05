def binarysearch(arr,i,j,x):
    if j >= i:
        mid = (i + j) // 2
        if arr[mid] == x:
            return 'element found at pos', mid
            
        elif arr[mid] > x:
            return binarysearch(arr,i,mid-1,x)
        else:
            return binarysearch(arr,mid+1,j,x)
    else:
        return 'not found'
        

    


arr = [2,5,2,2,6,8,9,3]
key = int(input("enter the element to be search:"))
result = binarysearch(arr,0,len(arr)-1,key)
print(result)
