import random
import numpy as np
import matplotlib.pyplot as plt


# Стороны from_x, to_x, from_y, to_y


def points_creator(number_of_points, side_a, side_b):
    return randomizer(number_of_points, 0, side_a, 0, side_b)


def randomizer(number_of_points, from_x, to_x, from_y, to_y):
    list_of_points_x = []
    list_of_points_y = []
    for i in range(number_of_points):
        list_of_points_x.append(round(random.uniform(from_x, to_x), 4))
        list_of_points_y.append(round(random.uniform(to_y, from_y, ), 4))
    return list_of_points_x, list_of_points_y


def position_check(list_of_points, task_lambda):
    list_of_points_x = list_of_points[0]
    list_of_points_y = list_of_points[1]
    list_of_true_points_x = []
    list_of_true_points_y = []
    list_of_false_points_x = []
    list_of_false_points_y = []

    for i in range(len(list_of_points_x)):
        point = [list_of_points_x[i], list_of_points_y[i]]
        if task_lambda(point[0], point[1]):
            list_of_true_points_x.append(point[0])
            list_of_true_points_y.append(point[1])
        else:
            list_of_false_points_x.append(point[0])
            list_of_false_points_y.append(point[1])

    return list_of_true_points_x, list_of_true_points_y, list_of_false_points_x, list_of_false_points_y


def position_check_for4(list_of_points):
    list_of_points_x = list_of_points[0]
    list_of_points_y = list_of_points[1]
    list_of_true_points_x = []
    list_of_true_points_y = []
    list_of_false_points_x = []
    list_of_false_points_y = []

    for i in range(len(list_of_points_x)):
        point = [list_of_points_x[i], list_of_points_y[i]]
        r = np.sqrt(point[0] ** 2 + point[1] ** 2)

        if point[0] > 0:
            fi = np.arctan(point[1] / point[0])
        elif point[0] < 0:
            fi = np.pi + np.arctan(point[1] / point[0])
        elif point[0] == 0 and point[1] > 0:
            fi = np.pi / 2
        elif point[0] == 0 and point[1] < 0:
            fi = - np.pi / 2
        else:
            fi = 0

        p = np.sqrt(21 * np.cos(fi) ** 2 + 1 * np.sin(fi) ** 2)
        if r < p:
            list_of_true_points_x.append(point[0])
            list_of_true_points_y.append(point[1])
        else:
            list_of_false_points_x.append(point[0])
            list_of_false_points_y.append(point[1])

    return list_of_true_points_x, list_of_true_points_y, list_of_false_points_x, list_of_false_points_y


def task_1(N=100):
    main_x = np.arange(0, 11, 1)
    main_y = np.arange(0, 21, 1)
    tack_lambda = lambda x, y: ((10 * x) / 10) < y < (10 * ((x - 20) / (-10)))
    a = 10
    b = 20
    main_list_of_points = points_creator(N, a, b)
    main_list_of_points = position_check(main_list_of_points, tack_lambda)
    M = len(main_list_of_points[0])
    S = round((M / N) * a * b, 4)
    S0 = 100

    print(f"\n1 Task"
          f"\nNumPoints : {N}:"
          f"\nTruePoints : {M}"
          f"\nSquareCalc : {S}"
          f"\nSquareTrue : {S0}")

    plt.figure(figsize=(10, 5))
    plt.plot(main_x, ((10 * main_x) / 10), 'g', linewidth=1)
    plt.plot(main_x, 10 * ((main_x - 20) / (-10)), 'g', linewidth=1)
    plt.plot(0 * main_y, main_y, 'r', linewidth=1)
    plt.plot([0, 0, a, a, 0], [0, b, b, 0, 0], 'b--', linewidth=0.4)
    plt.plot(main_list_of_points[0], main_list_of_points[1], 'g*')
    plt.plot(main_list_of_points[2], main_list_of_points[3], 'r*')
    plt.grid(True)
    plt.savefig('figure1.png')
    plt.show()


def task_2(N=150):
    main_x = np.arange(0, 5.1, 0.1)
    tack_lambda = lambda x, y: (np.sqrt(11 - 10 * np.sin(x) ** 2)) > y
    a = 5
    b = 5
    main_list_of_points = points_creator(N, a, b)
    main_list_of_points = position_check(main_list_of_points, tack_lambda)
    M = len(main_list_of_points[0])
    S = round((M / N) * a * b, 4)
    S0 = 11.2321  # подсчитано другим ресурсом

    print(f"\n2 Task"
          f"\nПри NumPoints : {N}:"
          f"\nTruePoints : {M}"
          f"\nSquareCalc : {S}"
          f"\nSquareTrue : {S0}")

    plt.figure(figsize=(10, 5))
    plt.plot(main_x, np.sqrt(11 - 10 * np.sin(main_x) ** 2), 'g', linewidth=1)
    plt.plot([0, 0, 5, 5, 0], [0, 5, 5, 0, 0], 'b--', linewidth=1)
    plt.plot(main_list_of_points[0], main_list_of_points[1], 'g*')
    plt.plot(main_list_of_points[2], main_list_of_points[3], 'r*')
    plt.grid(True)
    plt.savefig('figure2.png')
    plt.show()


def task_3(N=150):
    R = 10
    a = R * 2
    tack_lambda = lambda x, y: (x - R) ** 2 + (y - R) ** 2 < R ** 2
    main_list_of_points = points_creator(N, a, a)
    main_list_of_points = position_check(main_list_of_points, tack_lambda)
    M = len(main_list_of_points[0])
    S = round((M / N) * a ** 2, 4)
    S0 = np.pi * R ** 2
    pi = S / R ** 2

    print(f"\n3 Task"
          f"\nПри NumPoints : {N}:"
          f"\nTruePoints : {M}"
          f"\nSquareCalc : {S}"
          f"\nSquareTrue : {S0}"
          f"\npiCalc = {pi}"
          f"\npiTrue = {np.pi}")

    t = np.arange(0, 2 * np.pi, 0.01)

    plt.figure(figsize=(10, 10))
    plt.plot(R + R * np.cos(t), R + R * np.sin(t), 'g', linewidth=1)
    plt.plot([0, 0, a, a, 0], [0, a, a, 0, 0], 'b--', linewidth=0.4)
    plt.plot(main_list_of_points[0], main_list_of_points[1], 'g*')
    plt.plot(main_list_of_points[2], main_list_of_points[3], 'r*')
    plt.grid(True)
    plt.savefig('figure3.png')
    plt.show()


def task_4(N=170):
    a = 21
    b = 1
    main_list_of_points = randomizer(N, -6, 6, -3, 3)
    main_list_of_points = position_check_for4(main_list_of_points)
    M = len(main_list_of_points[0])
    S = round((M / N) * a * b, 4)
    S0 = 10.0849

    print(f"\n4 Task"
          f"\nNumPoints : {N}:"
          f"\nTruePoints : {M}"
          f"\nSquareCalc : {S}"
          f"\nSquareTrue : {S0}")

    t = np.arange(0, 2 * np.pi, 0.01)
    p = np.sqrt(21 * np.cos(t) ** 2 + 1 * np.sin(t) ** 2)

    plt.figure(figsize=(10, 10))
    plt.plot(p * np.cos(t), p * np.sin(t), 'g', linewidth=1)
    plt.plot([-6, -6, 6, 6, -6], [-3, 3, 3, -3, -3], 'b--', linewidth=1)
    plt.plot(main_list_of_points[0], main_list_of_points[1], 'g*')
    plt.plot(main_list_of_points[2], main_list_of_points[3], 'r*')
    plt.grid(True)
    plt.savefig('figure4.png')
    plt.show()


if __name__ == '__main__':
    print("\nChoose Task(1-4); For all(5):")
    task_num = int(input())
    print("\nCount of points(N):")
    count_of_points = int(input())

    if task_num == 5:
        task_1(count_of_points)
        task_2(count_of_points)
        task_3(count_of_points)
        task_4(count_of_points)
    elif task_num == 1:
        task_1(count_of_points)
    elif task_num == 2:
        task_2(count_of_points)
    elif task_num == 3:
        task_3(count_of_points)
    elif task_num == 4:
        task_4(count_of_points)
    else:
        print("\nError input")
