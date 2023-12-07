def reversestr(arr):
    new = []
    l = len(arr)-1
    for i in range(l,-1,-1):
        new.append(arr[i])
    return new
        

a = list(map(int,input("enter the comma seperated elements:").split()))
res = reversestr(a)
print("the result list is:",res)