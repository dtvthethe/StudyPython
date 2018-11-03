def tinh_tribonacy(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 3
    return tinh_tribonacy(n - 1) + tinh_tribonacy(n-2) + tinh_tribonacy(n-3)


print(tinh_tribonacy(101))
# fib_list = []
# for i in range(1, 101):
#     fib_list.append(tinh_tribonacy(i))
# print(fib_list)