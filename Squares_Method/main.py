import math
import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings(action='once')


def list_to_log(input_list):
    log_list = []
    for element in input_list:
        log_list.append(math.log(element))

    return log_list


def read_data(file_path):
    list_of_data = []
    with open(file_path, "r") as reader:
        for line in reader:
            list_of_data.append(float(line.split()[0]))

    return list_of_data


def least_squares_for_2(y_list, x_list):
    count_of_elements = len(y_list)
    iterator = 0
    A = ([0, 0, 0], [0, 0, 0])
    while iterator < count_of_elements:
        A[0][0] += x_list[iterator] ** 2
        A[0][1] += x_list[iterator]
        A[0][2] += x_list[iterator] * y_list[iterator]
        A[1][0] += x_list[iterator]
        A[1][1] = count_of_elements
        A[1][2] += y_list[iterator]
        iterator += 1

    determinant = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    if determinant != 0:  # Метод Крамера имеет одно решение
        a = round((A[0][2] * A[1][1] - A[0][1] * A[1][2]) / determinant, 2)
        b = round((A[0][0] * A[1][2] - A[0][2] * A[1][0]) / determinant, 2)
        return a, b

    return 0


def determinant3(matrix):
    return round(float(matrix[0][0] * matrix[1][1] * matrix[2][2] + \
                       matrix[0][1] * matrix[1][2] * matrix[2][0] + \
                       matrix[0][2] * matrix[1][0] * matrix[2][1] - \
                       matrix[0][2] * matrix[1][1] * matrix[2][0] - \
                       matrix[0][0] * matrix[1][2] * matrix[2][1] - \
                       matrix[0][1] * matrix[1][0] * matrix[2][2]), 4)


def least_squares_for_3(y_list, x_list):
    count_of_elements = len(y_list)
    iterator = 0
    matrix_A = ([0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0])
    while iterator < count_of_elements:
        matrix_A[0][0] += x_list[iterator] ** 4
        matrix_A[0][1] += x_list[iterator] ** 3
        matrix_A[0][2] += x_list[iterator] ** 2
        matrix_A[0][3] += (x_list[iterator] ** 2) * y_list[iterator]
        matrix_A[1][0] += x_list[iterator] ** 3
        matrix_A[1][1] += x_list[iterator] ** 2
        matrix_A[1][2] += x_list[iterator]
        matrix_A[1][3] += x_list[iterator] * y_list[iterator]
        matrix_A[2][0] += x_list[iterator] ** 2
        matrix_A[2][1] += x_list[iterator]
        matrix_A[2][2] = count_of_elements
        matrix_A[2][3] += y_list[iterator]
        iterator += 1

    matrix_by_three = [
        [matrix_A[0][0], matrix_A[0][1], matrix_A[0][2]], [matrix_A[1][0], matrix_A[1][1], matrix_A[1][2]],
        [matrix_A[2][0], matrix_A[2][1], matrix_A[2][2]]]
    matrix_determinant = determinant3(matrix_by_three)
    if matrix_determinant != 0:  # Cramer's method has one solution
        matrix_by_three = (
            [matrix_A[0][3], matrix_A[0][1], matrix_A[0][2]], [matrix_A[1][3], matrix_A[1][1], matrix_A[1][2]],
            [matrix_A[2][3], matrix_A[2][1], matrix_A[2][2]])
        a = round(float(determinant3(matrix_by_three) / matrix_determinant), 2)
        matrix_by_three = (
            [matrix_A[0][0], matrix_A[0][3], matrix_A[0][2]], [matrix_A[1][0], matrix_A[1][3], matrix_A[1][2]],
            [matrix_A[2][0], matrix_A[2][3], matrix_A[2][2]])
        b = round(float(determinant3(matrix_by_three) / matrix_determinant), 2)
        matrix_by_three = (
            [matrix_A[0][0], matrix_A[0][1], matrix_A[0][3]], [matrix_A[1][0], matrix_A[1][1], matrix_A[1][3]],
            [matrix_A[2][0], matrix_A[2][1], matrix_A[2][3]])
        c = round(float(determinant3(matrix_by_three) / matrix_determinant), 2)
        return a, b, c

    return 0


# Линейная функция
def linear_function(y_list, x_list):
    list_of_linear_function_values = []
    a, b = least_squares_for_2(y_list, x_list)  # y = ax + b
    for x in x_list:
        list_of_linear_function_values.append(round(a * x + b, 2))
    return list_of_linear_function_values, a, b


# Степенная функция
def degree_function(y_list, x_list):
    list_of_degree_function_values = []
    log_list_of_x = list_to_log(x_list)
    log_list_of_y = list_to_log(y_list)
    log_a, log_b = least_squares_for_2(log_list_of_y, log_list_of_x)
    log_b = math.exp(log_b)
    for x in x_list:  # y = b * x^a
        list_of_degree_function_values.append(round(log_b * x ** log_a, 2))
    return list_of_degree_function_values, log_a, log_b


# Показательная функция
def exponential_function(y_list, x_list):
    list_of_exponential_function_values = []
    log_list_of_y = list_to_log(y_list)
    poc_a, poc_b = least_squares_for_2(log_list_of_y, x_list)
    poc_b = math.exp(poc_b)
    for x in x_list:  # y = b * exp^ax
        list_of_exponential_function_values.append(round(poc_b * math.exp(x * poc_a), 2))
    return list_of_exponential_function_values, poc_a, poc_b


# Квадратичная функция
def quadratic_function(y_list, x_list):
    list_of_quadratic_function_values = []
    a, b, c = least_squares_for_3(y_list, x_list)  # y = ax + b
    for x in x_list:
        list_of_quadratic_function_values.append(round(a * x ** 2 + b * x + c, 2))
    return list_of_quadratic_function_values, a, b, c


# Погрешность
def rate(y_list, z_list):
    ans = 0
    number_of_elements = len(y_list)
    iterator = 0
    while iterator < number_of_elements:
        ans += (y_list[iterator] - z_list[iterator]) ** 2
        iterator += 1
    return round(ans, 2)


if __name__ == '__main__':
    check = input("Выберете вариант: Индивидуальный(1) или Контрольный(2) : ")
    if check == "1":
        main_list_of_x = read_data("data_x.txt")
        main_list_of_y = read_data("data_y.txt")
    elif check == "2":
        main_list_of_x = read_data("datatest_x.txt")
        main_list_of_y = read_data("datatest_y.txt")
    else:
        print("Ошибка выбора варианта")
        exit()

    z_lin, a_lin, b_lin = linear_function(main_list_of_y, main_list_of_x)
    z_deg, a_deg, b_deg = degree_function(main_list_of_y, main_list_of_x)
    z_exp, a_exp, b_exp = exponential_function(main_list_of_y, main_list_of_x)
    z_quad, a_quad, b_quad, c_quad = quadratic_function(main_list_of_y, main_list_of_x)

    dict_of_error = {"Линейная функция": rate(main_list_of_y, z_lin),
                     "Степенная функция": rate(main_list_of_y, z_deg),
                     "Показательная функция": rate(main_list_of_y, z_exp),
                     "Квадратичная функция": rate(main_list_of_y, z_quad)}

    print("\nВ данной задаче лучшей аппроксимирующей функцией является: ", end='')
    print(min(dict_of_error, key=dict_of_error.get), "\nИтоговая погрешность каждой функции:")
    print("Линейная функция = ", dict_of_error["Линейная функция"], "a = ", a_lin, "b = ", b_lin,
          "\nСтепенная функция = ", dict_of_error["Степенная функция"], "a = ", a_deg, "b = ", b_deg,
          "\nПоказательная функция = ", dict_of_error["Показательная функция"], "a = ", a_exp, "b = ", b_exp,
          "\nКвадратичная функция = ", dict_of_error["Квадратичная функция"], "a = ", a_quad, "b = ", b_quad, "c = ", c_quad

          )

    plt.figure(figsize=(10, 5), )
    plt.plot(main_list_of_x, main_list_of_y, 'ro')
    plt.plot(main_list_of_x, z_lin, label=r'$f_1(x)=ax+b$')  # Линейная функция
    plt.plot(main_list_of_x, z_deg, label=r'$f_2(x)=bx^a$')  # Степенная функция
    plt.plot(main_list_of_x, z_exp, label=r'$f_3(x)=be^{ax}$')  # Показательная функция
    plt.plot(main_list_of_x, z_quad, label=r'$f_4(x)=ax^2+bx+c$')  # Квадратичная функция
    plt.xlabel(r'$x$', fontsize=14)
    plt.ylabel(r'$f(x)$', fontsize=14)
    plt.grid(True)
    plt.legend(loc='best', fontsize=12)
    plt.savefig('figure_with_legend.png')
    plt.show()
