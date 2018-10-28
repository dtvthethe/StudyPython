try:
    a = 5/0
except ZeroDivisionError as ex:
    print(ex)
except BaseException as ex:
    print(ex)
finally:
    print('Done')