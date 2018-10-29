def ham_bat_tu():
    try:
        print('Ham bat tu')
        a = 5/0
    except ZeroDivisionError as ex:
        print(ex)
    except BaseException as ex:
        print(ex)
    finally:
        ham_bat_tu()


ham_bat_tu()