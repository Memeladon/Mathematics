import math
import matplotlib.pyplot as plt

# Функции 1 задачи
g_function = lambda x, y, z: -2 * z + 4 * y  # x'
f_function = lambda x, y, z: -z + 3 * y  # y'
gt_function = lambda t: 4 * math.exp(-t) - math.exp(2 * t)  # x
ft_function = lambda t: math.exp(-t) - math.exp(2 * t)  # y
# Функции 2 задачи
g1_function = lambda x, y, z: y  # x'
f1_function = lambda x, y, z: 2 * y  # y'
gt1_function = lambda t: math.exp(2 * t) + 1  # x
ft1_function = lambda t: 2 * math.exp(2 * t)  # y


def runge_kutta(h, y0, z0, g, f, x0=0):
    answer_y = [y0]
    answer_z = [z0]
    answer_x = [x0]
    y = y0
    z = z0

    while x0 < 1:
        k1 = h * f(x0, y, z)
        l1 = h * g(x0, y, z)
        k2 = h * f(x0 + h / 2, y + k1 / 2, z + l1 / 2)
        l2 = h * g(x0 + h / 2, y + k1 / 2, z + l1 / 2)
        k3 = h * f(x0 + h / 2, y + k2 / 2, z + l2 / 2)
        l3 = h * g(x0 + h / 2, y + k2 / 2, z + l2 / 2)
        k4 = h * f(x0 + h, y + k3, z + l3)
        l4 = h * g(x0 + h, y + k3, z + l3)

        delta_y = round((k1 + 2 * k2 + 2 * k3 + k4) / 6, 9)
        delta_z = round((l1 + 2 * l2 + 2 * l3 + l4) / 6, 9)
        y = round(y + delta_y, 9)
        z = round(z + delta_z, 9)
        answer_y.append(y)
        answer_z.append(z)
        x0 = round(x0 + h, 9)
        answer_x.append(x0)
    return answer_x, answer_y, answer_z


def set_true(list_x, gt, ft):
    list_true_z = []
    list_true_y = []
    for x in list_x:
        list_true_y.append(round(ft(x), 9))
        list_true_z.append(round(gt(x), 9))
    return list_true_y, list_true_z


def plot(x, y, z, true_y, true_z, n):
    plt.title('Метод Рунге-Кутта', fontsize=20, fontname='Times New Roman')
    if n == 1:
        plt.plot(x, true_y, 'lime', label=r'Точное решение для y(t)')
        plt.plot(x, true_z, 'r', label=r'Точное решение для x(t)')
        plt.plot(x, y, 'b--', label=r'Метод Рунге-Кутта для для y(t)')
        plt.plot(x, z, 'y--', label=r'Метод Рунге-Кутта для для x(t)')
        plt.xlabel(r'$t$', fontsize=14)
        plt.ylabel(r'$f(t)$', fontsize=14)
        plt.grid(True)
        plt.legend(loc='best', fontsize=10)
        plt.savefig('1.png')
        plt.show()
    else:
        plt.plot(z, y, 'purple', label=r'Метод Рунге-Кутта')
        plt.plot(z, y, 'b.', label=r'Метод Рунге-Кутта')
        plt.plot(true_z, true_y, 'y--', label=r'Точное решение')
        plt.plot(true_z, true_y, 'r+', label=r'Точное решение')
        plt.xlabel(r'$x$', fontsize=14)
        plt.ylabel(r'$y$', fontsize=14)
        plt.grid(True)
        plt.legend(loc='best', fontsize=10)
        plt.savefig('2.png')
        plt.show()


def print_inf(x, y, z, true_y, true_z):
    print("   x:   " + str(x))
    print("   y:   " + str(y))
    print("   z:   " + str(z))
    print("True y: " + str(true_y))
    print("True z: " + str(true_z))


if __name__ == '__main__':
    choose = int(input("Выберите пример для теста:\n"
                       "[1] Первый тест\n"
                       "[2] Второй тест\n"))
    step = float(input("Введите шаг: "))

    if choose == 1:
        x, y, z = runge_kutta(step, 0, 3, g_function, f_function)
        true_y, true_z = set_true(x, gt_function, ft_function)

        nnt = input("Вывести значения? [д/н]: ")
        if nnt == "д" or nnt == "Д":
            print_inf(x, y, z, true_y, true_z)

        plot(x, y, z, true_y, true_z, 1)
        plot(x, y, z, true_y, true_z, 2)

    elif choose == 2:
        x, y, z = runge_kutta(step, 2, 2, g1_function, f1_function)
        true_y, true_z = set_true(x, gt1_function, ft1_function)

        nnt = input("Вывести значения? [д/н]: ")
        if nnt == "д" or nnt == "Д":
            print_inf(x, y, z, true_y, true_z)

        plot(x, y, z, true_y, true_z, 1)
        plot(x, y, z, true_y, true_z, 2)
    else:
        print("Ошибка ввода!")
