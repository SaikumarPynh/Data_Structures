def LinearSearch(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return 'Element found at index' ,+i 
    return "elenement is not found"



arr = [2,4,2,5,7,9]
x = int(input("enter the element to be found:"))
res = LinearSearch(arr,x)
print(res)
