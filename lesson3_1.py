def func_calc(*args):
    var_1 = int(input("Введите первое число "))
    var_2 = int(input("Введите второне число "))
    if var_2 != 0:
        return var_1 / var_2
    else:
        print("На ноль делить нельзя!")

    '''
    try:
        var_1 = int(input("Введите первое число "))
        var_2 = int(input("Введите второне число "))
        var_3 = var_1 / var_2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "На ноль делить нельзя!"

    return var_3

    '''


print(f"Результат  {func_calc()}")
