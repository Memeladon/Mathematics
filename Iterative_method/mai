from math import ceil
from prettytable import PrettyTable
import random


# Отрисовка в консоль
def table_draw(td, th, columns):
    table = PrettyTable(th)
    while td:
        # Используя срез добавляем первые columns элементa в строку.
        table.add_row(td[:columns])
        # Используя срез переопределяем td так, чтобы он
        # больше не содержал первых columns элементов.
        td = td[columns:]

    print("\n{}".format(table))  # Печатаем таблицу


# Интерфейс не сделан пока что
def quad_interface():
    print("Метод Квадратов.\n"
          "Вы хотите ввести начальное n-разрядное число? [д/н]\n"
          "В случае отказа будет использована случайная величина."
          "[0] Для выхода.")
    answer = input()

    if answer == '0':
        exit()
    elif answer == 'д' or answer == 'Д':
        n = int(input("Введите целочисленное n: "))
        quad_rnd_gen(n)
    elif answer == 'н' or answer == 'Н':
        quad_rnd_gen()
    else:
        "Нераспознанный символ. Повторите попытку."
        quad_interface()


# %|----------------------% Main functions %----------------------\% #
# Серединные квадраты
def quad_rnd_gen(initN=None, steps=5):
    # Если получили пустое значение
    if initN is None:
        initN = random.randrange(1, 100000)

    td = []

    for i in range(steps):
        quad = initN ** 2  # Возвели в квадрат
        current = '{0:,}'.format(quad).replace(',', ' ')  # Число -> строка с разделителями
        middle = current[ceil(len(current) / 4):int(len(current) - int(len(current) / 4))].replace(' ', '')
        rnd_num = int(middle) / pow(10, int(len(middle)))  # Случайное число

        td.extend(['{0:,}'.format(initN).replace(',', ' '),
                   current,
                   rnd_num])
        initN = int(middle)

    table_draw(td, ["Исх. Число", "Квадрат", "Случайное число"], 3)


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

    for i in range(steps):
        multiply = initM * initN  # Умножили ядро на множимое
        current = '{0:,}'.format(multiply).replace(',', ' ')  # Число -> строка с разделителями
        middle = current[ceil(len(current) / 4):int(len(current) - ceil(len(current) / 4))].replace(' ', '')
        rnd_num = int(middle) / pow(10, len(middle))  # Случайное число

        td.extend(['{0:,}'.format(initN).replace(',', ' '),
                   current,
                   rnd_num])

        initN = int(current[int(len(current) / 2):].replace(' ', ''))

    table_draw(td, ["Множимое", "Произведение", "Случайное число"], 3)


# Мультипликативный конгруэнтный
def congruent_rnd_gen(initN=None, initD=None, steps=5):
    # Если получили пустое значение
    if initN is None:
        # initN = Множитель -постоянная
        initN = random.randrange(1, 10000)
    if initD is None:
        # initD = Делитель -постоянная
        initD = random.randrange(1, 10000)

    td = []
    current = initN

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
        current = remain

    table_draw(td, ["Исх. число", "Произведение", "Частное, целая часть", "Остаток", "Случайное число"], 5)


if __name__ == '__main__':
    quad_rnd_gen(7153)  # 7153
    composition_rnd_gen(5167, 3729)  # 5167, 3729
    congruent_rnd_gen(1357, 5689)  # 1357, 5689
