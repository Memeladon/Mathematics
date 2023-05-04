import subprocess
import sys
import logging
import os

import config
from PySide2 import QtWidgets
from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide2.QtWidgets import *
from simulate import simulation
from config import task_list

#Логирование
logging.basicConfig(format='[%(levelname) 5s/%(as ctime)s] %(name)s: %(message)s', level=logging.INFO)

class Ui_Computer(object):
    def setupUi(self, Computer):
        if not Computer.objectName():
            Computer.setObjectName(u"Computer")
        Computer.resize(720, 640)
        self.centralwidget = QWidget(Computer)
        self.centralwidget.setObjectName(u"centralwidget")

        # ~~~~~~~~~~~~~~~~~~~~~~~~~ ПЕРВЫЙ БОКС ~~~~~~~~~~~~~~~~~~~~~~~~~ #
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 700, 240))

        # Количество повторений программы
        self.label_count = QLabel(self.groupBox)
        self.label_count.setObjectName(u"label_count")
        self.label_count.setGeometry(QRect(20, 30, 240, 13))

        self.line_count = QLineEdit(self.groupBox)
        self.line_count.setText(task_list[8])
        self.line_count.setObjectName(u"line_count")
        self.line_count.setGeometry(QRect(263, 30, 30, 20))

        # Интервал поступления заданий
        self.label_task_intervals = QLabel(self.groupBox)
        self.label_task_intervals.setObjectName(u"label_task_intervals")
        self.label_task_intervals.setGeometry(QRect(20, 60, 240, 13))

        self.line_task_intervals_1 = QLineEdit(self.groupBox)
        self.line_task_intervals_1.setText(task_list[6])
        self.line_task_intervals_1.setObjectName(u"line_task_intervals_1")
        self.line_task_intervals_1.setGeometry(QRect(263, 60, 30, 20))

        self.label_plus = QLabel(self.groupBox)
        self.label_plus.setObjectName(u"label_plus")
        self.label_plus.setGeometry(QRect(303, 60, 240, 13))

        self.line_task_intervals_2 = QLineEdit(self.groupBox)
        self.line_task_intervals_2.setText(task_list[7])
        self.line_task_intervals_2.setObjectName(u"line_task_intervals_2")
        self.line_task_intervals_2.setGeometry(QRect(323, 60, 30, 20))

        # Вероятность на 1ую ЭВМ при первом вхождении задания
        self.label_1computer = QLabel(self.groupBox)
        self.label_1computer.setObjectName(u"label_1computer")
        self.label_1computer.setGeometry(QRect(400, 90, 240, 13))

        self.line_p1 = QLineEdit(self.groupBox)
        self.line_p1.setText(task_list[1])
        self.line_p1.setObjectName(u"line_p1")
        self.line_p1.setGeometry(QRect(654, 90, 30, 20))

        # Вероятность на 2ую ЭВМ при первом вхождении задания
        self.label_2computer = QLabel(self.groupBox)
        self.label_2computer.setObjectName(u"label_2computer")
        self.label_2computer.setGeometry(QRect(400, 120, 240, 13))

        self.line_p2 = QLineEdit(self.groupBox)
        self.line_p2.setText(task_list[2])
        self.line_p2.setObjectName(u"line_p2")
        self.line_p2.setGeometry(QRect(654, 120, 30, 20))

        # Вероятность поступление после прохождения первой ЭВМ
        self.label_computer_after = QLabel(self.groupBox)
        self.label_computer_after.setObjectName(u"label_computer_after")
        self.label_computer_after.setGeometry(QRect(400, 30, 250, 13))

        # Вероятность на 2ую ЭВМ после прохождения первой ЭВМ
        self.label_2computer_after = QLabel(self.groupBox)
        self.label_2computer_after.setObjectName(u"label_2computer_after")
        self.label_2computer_after.setGeometry(QRect(400, 60, 250, 13))

        self.line_p4 = QLineEdit(self.groupBox)
        self.line_p4.setText(task_list[4])
        self.line_p4.setObjectName(u"line_p3")
        self.line_p4.setGeometry(QRect(654, 60, 30, 20))

        # Количество заданий
        self.task_count = QLabel(self.groupBox)
        self.task_count.setObjectName(u"task_count")
        self.task_count.setGeometry(QRect(400, 150, 250, 13))

        self.line_p6 = QLineEdit(self.groupBox)
        self.line_p6.setText(task_list[0])
        self.line_p6.setObjectName(u"line_p6")
        self.line_p6.setGeometry(QRect(654, 150, 30, 20))

        # Кнопка подверждения
        self.button_apply = QPushButton(self.groupBox)
        self.button_apply.setObjectName(u"button_apply")
        self.button_apply.setGeometry(QRect(18, 190, 101, 31))

        # Кнопка запуска
        self.button_start = QPushButton(self.groupBox)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setGeometry(QRect(180, 190, 101, 31))

        # ~~~~~~~~~~~~~~~~~~~~~~~~~ ВТОРОЙ БОКС ~~~~~~~~~~~~~~~~~~~~~~~~~ #
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 260, 700, 350))

        # Список результатов
        self.plainTextEdit = QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setGeometry(QRect(20, 30, 660, 310))

        # Это надо
        Computer.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Computer)
        self.statusbar.setObjectName(u"statusbar")
        Computer.setStatusBar(self.statusbar)
        self.retranslateUi(Computer)
        QMetaObject.connectSlotsByName(Computer)

    def retranslateUi(self, Computer):
        Computer.setWindowTitle(QCoreApplication.translate("Computer", u"Симуляция ЭВМ", None))
        self.groupBox.setTitle(QCoreApplication.translate("Computer", u"Входные данные", None))

        self.label_count.setText(QCoreApplication.translate("Computer", u"Количество повторений симуляции:", None))
        self.label_task_intervals.setText(QCoreApplication.translate("Computer", u"Интервал поступления заданий:", None))
        self.label_plus.setText(QCoreApplication.translate("Computer", u"+", None))
        self.label_1computer.setText(QCoreApplication.translate("Computer", u"Вероятность поступления на 1ую ЭВМ:", None))
        self.label_2computer.setText(QCoreApplication.translate("Computer", u"Вероятность поступления на 2ую ЭВМ:", None))

        self.label_computer_after.setText(QCoreApplication.translate("Computer", u"Вероятности поступления после 1ого ЭВМ:", None))
        self.label_2computer_after.setText(QCoreApplication.translate("Computer", u"Вероятность поступления на 2ую ЭВМ:", None))
        self.task_count.setText(QCoreApplication.translate("Computer", u"Количество заданий на ЭВМ:", None))
        self.button_apply.setText(QCoreApplication.translate("Computer", u"Подтвердить", None))
        self.button_start.setText(QCoreApplication.translate("Computer", u"Запустить", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("Computer", u"Результаты работы", None))
        self.plainTextEdit.setPlaceholderText("")
        self.plainTextEdit.setReadOnly(True)


class Draw(QtWidgets.QMainWindow, Ui_Computer):  # Собираем класс с нашими основными действиями
    subproc: None  # переменная для хранения номера подпроцесса

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Создание формы и Ui (наш дизайн)
        self.show()  # Показать наше окно
        # прописывем реакции на кнопки
        self.button_start.clicked.connect(self.start)
        self.button_apply.clicked.connect(self.apply)


    def start(self):  # функция которая запускает работу программы
        process = subprocess.Popen("simulate.py", shell=True)  # запускаем скрипт с программой в отдельном подпроцессе
        self.subproc = process.pid  # сохраняем номер подпроцесса
    def apply(self):
        # task_list = [task_count, p1st, p2nd, p2nd_after, interval1, interval2, repeat_count]

        task_list[0] = self.line_p6.text()                # Количество заданий
        task_list[1] = self.line_p1.text()                # Вероятность на первую ЭВМ
        task_list[2] = self.line_p2.text()                # Вероятность на вторую ЭВМ
        task_list[3] = self.line_p4.text()                # Вероятность на вторую ЭВМ (ПОСЛЕ ПРОХОЖДЕНИЯ ПЕРВОЙ ЭВМ)
        task_list[4] = self.line_task_intervals_1.text()  # Первый интервал
        task_list[5] = self.line_task_intervals_2.text()  # Отклонение интервала
        task_list[6] = self.line_count.text()             # Количество повторений задания

        output = open("config.py", 'w')  # перезаписываем новые даные в файл конфига
        print("task_list =", task_list, file=output)
        output.close()  # закрываем файл

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    Computer = Draw()  # Содание инстанса класса Калькулятор, который мы создадим далее
    sys.exit(app.exec_())  # Запуск