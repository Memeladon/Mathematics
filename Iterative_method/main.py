# import csv
import random

import pandas as pd
import matplotlib.pyplot as plt

from prettytable import PrettyTable


# %|----------------------% Misc functions %----------------------\% #

# Отрисовка в консоль
def table_draw(td, th, columns):
    table = PrettyTable(th)
    while td:
        # Используя срез добавляем первые columns элементa в строку.
        table.add_row(td[:columns])
        # Используя срез переопределяем td так, чтобы он
        # больше не содержал первых columns элементов.
        td = td[columns:]

    print("{}".format(table))  # Печатаем таблицу


# Интерфейс не сделан пока что
def interface():
    ans = int(input("Выберете задачу:\n"
                    "[1] Метод квадратов\n"
                    "[2] Метод произведений\n"
                    "[3] Мультипликативный конгруэнтный метод\n"
                    "[0] Выход\n"))
    if ans == 0:
        exit()
    elif ans == 1:
        print("[None - для значения по умолчанию]")
        n = input("Введите параметр n: ")
        stp = input("Введите количество итераций: ")

        if n == "None":
            if stp == "None":
                quad_rnd_gen(None, 5)
            else:
                quad_rnd_gen(None, int(stp))
        elif stp == "None":
            quad_rnd_gen(int(n), 5)
        else:
            quad_rnd_gen(int(n), int(stp))

    elif ans == 2:
        print("[None - для значения по умолчанию]")
        m = input("Введите значение 'ядра': ")
        n = input("Введите значение 'множимого': ")
        stp = input("Введите количество итераций: ")

        if m == "None":
            if n == "None":
                if stp == "None":
                    composition_rnd_gen(None, None, 5)
                else:
                    composition_rnd_gen(None, None, int(stp))
            elif stp == "None":
                composition_rnd_gen(None, int(n), 5)
            else:
                composition_rnd_gen(None, int(n), int(stp))
        elif n == "None":
            if stp == "None":
                composition_rnd_gen(int(m), None, 5)
            else:
                composition_rnd_gen(int(m), None, int(stp))
        elif stp == "None":
            composition_rnd_gen(int(m), int(n), 5)
        else:
            composition_rnd_gen(int(m), int(n), int(stp))

    elif ans == 3:
        print("[None - для значения по умолчанию]")
        m = input("Введите значение 'ядра': ")
        n = input("Введите значение 'делителя': ")
        stp = input("Введите количество итераций: ")

        if m == "None":
            if n == "None":
                if stp == "None":
                    congruent_rnd_gen(None, None, 5)
                else:
                    congruent_rnd_gen(None, None, int(stp))
            elif stp == "None":
                congruent_rnd_gen(None, int(n), 5)
            else:
                congruent_rnd_gen(None, int(n), int(stp))
        elif n == "None":
            if stp == "None":
                congruent_rnd_gen(int(m), None, 5)
            else:
                congruent_rnd_gen(int(m), None, int(stp))
        elif stp == "None":
            congruent_rnd_gen(int(m), int(n), 5)
        else:
            congruent_rnd_gen(int(m), int(n), int(stp))


# Попытка сделать отрисовку графиком
def plot(val=None, name=None):
    list_x = [x / 10 for x in range(11)]
    s = pd.Series(val)

    # plt.axis([0, 1, 0, len(val)])
    plt.hist(s, color='blue', edgecolor='black', facecolor='C0', alpha=0.75, bins=list_x)
    plt.title(name)
    plt.ylabel('Количество чисел в интервале')
    plt.xlabel('Интервал')
    plt.show()

    # ----ЭТО НА СЛУЧАЙ ОТРИСОВКИ НЕСКОЛЬКОХ ГРАФИКОВ---- #
    # names = ['group_a', 'group_b', 'group_c']
    # values = [1, 10, 100]
    #
    # plt.figure(figsize=(9, 3))
    #
    # plt.subplot(131)
    # plt.bar(names, values)
    # plt.subplot(132)
    # plt.scatter(names, values)
    # plt.subplot(133)
    # plt.plot(names, values)
    # plt.suptitle('Categorical Plotting')
    # plt.show()


# Метод квадратов
def quad_rnd_gen(initN=None, steps=5):
    # Если получили пустое значение
    if initN is None:
        initN = random.randrange(1, 100000)

    td = []
    val = []
    print("\n[1] Метод квадратов")

    for i in range(steps):
        quad = initN ** 2  # Возвели в квадрат
        current = '{0:,}'.format(quad).replace(',', '')  # Число -> строка с разделителями
        middle = current[int(len(current) / 4):-int(len(current) / 4)]
        rnd_num = int(middle) / pow(10, int(len(middle)))  # Случайное число

        td.extend(['{0:,}'.format(initN).replace(',', ' '),
                   '{0:,}'.format(quad).replace(',', ' '),
                   rnd_num])
        val.append(rnd_num)
        initN = int(middle)

    # table_draw(td, ["Исх. Число", "Квадрат", "Случайное число"], 3)
    plot(val, name="Метод квадратов")


# Произведения
def composition_rnd_gen(initM=None, initN=None, steps=5):
    # Если получили пустое значение
    if initN is None:
        # initN = Множимое
        initN = random.randrange(1, 10000)
    if initM is None:
        # initM = Ядро -постоянная
        initM = random.randrange(1, 10000)

    td = []
    val = []
    print("\n[2] Метод произведений")

    for i in range(steps):
        multiply = initM * initN  # Умножили ядро на множимое
        current = '{0:,}'.format(multiply).replace(',', '')  # Число -> строка с разделителями
        middle = current[int(len(current) / 4):-int(len(current) / 4)]
        rnd_num = int(middle) / pow(10, len(middle))  # Случайное число

        td.extend(['{0:,}'.format(initN).replace(',', ' '),
                   '{0:,}'.format(multiply).replace(',', ' '),
                   rnd_num])
        val.append(rnd_num)
        initN = int(current[int(len(current) / 2):].replace(' ', ''))

    # table_draw(td, ["Множимое", "Произведение", "Случайное число"], 3)
    plot(val, name="Метод произведений")


# Мультипликативный конгруэнтный
def congruent_rnd_gen(initN=None, initD=None, steps=5):
    # Если получили пустое значение
    if initN is None:
        # initN = Множитель -постоянная
        initN = random.randrange(1, 10000)
    if initD is None:
        # initD = Делитель -постоянная
        initD = random.randrange(1, 10000)

    val = []
    td = []
    current = initN
    print("\n[3] Мультипликативный конгруэнтный метод")

    for i in range(steps):
        multiply = current * initN  # Умножение
        whole = multiply // initD  # Целая часть
        remain = multiply % initD  # Остаток
        rnd_num = remain / pow(10, len(str(remain)))  # Случайное число

        td.extend(['{0:,}'.format(current).replace(',', ' '),
                   '{0:,}'.format(multiply).replace(',', ' '),
                   '{0:,}'.format(whole).replace(',', ' '),
                   '{0:,}'.format(remain).replace(',', ' '),
                   '{0:,}'.format(rnd_num).replace(',', ' ')])
        val.append(rnd_num)
        current = remain

    # table_draw(td, ["Исх. число", "Произведение", "Частное, целая часть", "Остаток", "Случайное число"], 5)
    plot(val, name="Мультипликативный конгруэнтный метод")


if __name__ == '__main__':
    interface()
    # quad_rnd_gen()  # 7153
    # composition_rnd_gen()  # 5167, 3729
    # congruent_rnd_gen()  # 1357, 5689
