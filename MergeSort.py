def mergesort(list):
    
    if len(list) > 1:
        mid = len(list) // 2
        left_list = list[ :mid]
        right_list = list[mid:]
        #for deviding the list upto a single element for a list
        mergesort(left_list)
        mergesort(right_list)
        i = 0
        j = 0
        k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                k = k + 1
                i = i + 1
            else:
                list[k] = right_list[j]
                k = k + 1
                j = j + 1
        # if any elements in left list are left
        while i < len(left_list):
            list[k] = left_list[i]
            k = k + 1
            i = i + 1
        # if any elements in right list are left
        while j < len(right_list):
            list[k] = right_list[j]
            k = k + 1
            j = j + 1




#driver code
n = int(input("enter the length of the list:"))
list = [int(input()) for i in range(n)]
mergesort(list)
print("the list after sorted is:",list)