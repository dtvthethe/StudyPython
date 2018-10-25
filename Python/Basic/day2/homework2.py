#Bubble sort:
def bubble_sort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

#INPUT
input = '[12, 25, 38, 18, 16]'

#PROCESS
arr = []
#Step 1: Remove space and [ ] symbols
str_tmp = input[1 : len(input)-2].replace(' ','').replace('[','').replace(']','')
#Step 2: Split by , symbols => array type str
arr_split = str_tmp.split(',')
#Step 3: Convert each item from string type to integer type
for item in arr_split:
    arr.append(int(item))

#Step 4: Sort the list:
bubble_sort(arr)

#OUTPUT
print(arr)
print(type(arr))





