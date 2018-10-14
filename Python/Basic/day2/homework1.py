import ast

#INPUT
input = '[12, 25, 38, 18, 16]'

#PROCESS
#Step 1: Convert the str_input to list
arr = ast.literal_eval(input)

#Step 2: Sort the list:
arr.sort(reverse=False)

#OUTPUT
print(arr)
print(type(arr))





