# cc = 8

# for x in range(0,8):
# 	for y in range(0,8):
# 		if 

for i in range(0, 8):
    s = ''
    for j in range(0, 8):
        if j in [i, 8-i-1]:
            s += '*'
        else:
            s += ' '
    print(s)