import csv
import random
import seaborn as sns

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
                    "[4] Все выше перечисленные\n"
                    "[0] Выход\n"))
    if ans == 0:
        exit()
    elif ans == 1:
        quad_rnd_gen()
    elif ans == 2:
        composition_rnd_gen()
    elif ans == 3:
        congruent_rnd_gen()
    elif ans == 4:
        quad_rnd_gen()
        composition_rnd_gen()
        congruent_rnd_gen()

# Попытка сделать отрисовку графиком
def plot():
    list_x = [(x + 1) / 10 for x in range(10)]

    val = sns.load_dataset("values")
    val.head()
    # sns.displot(tips, x="size", bins=list_x)

# По фану - самая простая записть в csv
def scv_write(val):
    with open('values.csv', 'w', newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=' ', quotechar='|')
        write.writerow(val)


# %|----------------------% Main functions %----------------------\% #
# Серединные квадраты
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

    table_draw(td, ["Исх. Число", "Квадрат", "Случайное число"], 3)
    scv_write(val)
    plot()


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

    table_draw(td, ["Множимое", "Произведение", "Случайное число"], 3)
    plot(val)


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

    table_draw(td, ["Исх. число", "Произведение", "Частное, целая часть", "Остаток", "Случайное число"], 5)
    plot(val)


if __name__ == '__main__':
    # interface()
    quad_rnd_gen()  # 7153
    # composition_rnd_gen()  # 5167, 3729
    # congruent_rnd_gen(1357, 5689)  # 1357, 5689
