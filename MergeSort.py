def mergesort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left_list = list[ :mid]
        right_list = list[mid:]
        #for deviding the list upto a single element for a list
        mergesort(left_list)
        mergesort(right_list)
        i = 0 #for index of left list
        j = 0#for index of right list
        k = 0#for index of new list here new list is the initially taken list the is list
        while i < len(left_list) and j < len(right_list):
            # suppose list1 = [2,4,6] and list2 = [1,10,15] are sorted list when merging these two
            # 1st ele of list1 is comp with 1st ele of list2 since sorted lists if ele is lesser
            # # then it is the small it has to be put into the final list
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