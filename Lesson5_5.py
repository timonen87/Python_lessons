'''
    Создать (программно) текстовый файл, записать в него программно
    набор чисел, разделенных пробелами. Программа должна
    подсчитывать сумму чисел в файле и выводить ее на экран.
'''

def summ():
    try:
        with open('file4.txt', 'w') as f_obj:
            numm = input('Введите цифры через пробел ')
            f_obj.writelines(numm)
            my_summ = numm.split()

            print(sum(map(int, my_summ)))         
    except IOError:
        print("Произошла ошибка ввода-вывода!")
    except ValueError:
        print('Непраильно введены числа, введите числа через пробел')
summ()
