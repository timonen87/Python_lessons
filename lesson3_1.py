

def func_calc(*args):

    try:
        var_1 = int(input("Введите первое число "))
        var_2 = int(input("Введите второне число "))
        res = var_1 / var_2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "На ноль делить нельзя!"

    return res
    
    '''
    вариант через if
    
    if var_2 != 0:
        return var_1 / var_2
    else:
        print("На ноль делить нельзя!")
    '''


print(f"Результат  {func_calc()}")
