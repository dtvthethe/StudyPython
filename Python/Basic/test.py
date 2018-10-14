#INPUT
arr = [12, 25, 38, 18, 16]

for about in range(len(arr)-1,0,-1):
    for inn in range(about):
        if arr[inn] > arr[inn+1]:
            tmp = arr[inn]
            arr[inn] = arr[inn+1]
            arr[inn+1] = tmp

for about in range(len(arr)-1,0,-1):
    print('about ', about)
    for i in range(about):
        print('i = ', i)
