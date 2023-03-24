import random

from collections import deque
from datetime import timedelta, datetime


class time_generate:
    @staticmethod
    def random_date(start, end):
        """
        Возвращает случайное значение между датами
        """
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = random.randrange(int_delta)
        return timedelta(seconds=random_second)

    @staticmethod
    def sum_date(timeList=None):
        # timeList = ['0:00:00', '0:00:15', '9:30:56']
        if timeList is None:
            timeList = ['0:00:00', '0:00:00']
        totalSecs = 0
        for tm in timeList:
            timeParts = [int(s) for s in tm.split(':')]
            totalSecs += (timeParts[0] * 60 + timeParts[1]) * 60 + timeParts[2]
        totalSecs, sec = divmod(totalSecs, 60)
        hr, min = divmod(totalSecs, 60)
        return str("%d:%02d:%02d" % (hr, min, sec))


class simulation:
    first_computer = lambda: time_generate.random_date(datetime.strptime('00:03:00', '%H:%M:%S'),
                                                       datetime.strptime('00:05:00', '%H:%M:%S'))
    second_computer = lambda: time_generate.random_date(datetime.strptime('00:02:00', '%H:%M:%S'),
                                                        datetime.strptime('00:04:00', '%H:%M:%S'))
    third_computer = lambda: time_generate.random_date(datetime.strptime('00:03:00', '%H:%M:%S'),
                                                       datetime.strptime('00:07:00', '%H:%M:%S'))

    def __init__(self):
        self.first, self.second, self.third = [], [], []
        self.fst_count, self.snd_count, self.trd_count = 0, 0, 0
        self.cur1, self.cur2, self.all = timedelta(), timedelta(), timedelta(hours=0, minutes=0, seconds=0)

    def time_counter(self, tasks=200):
        que = deque([i for i in range(tasks)])

        while len(que) != 0:
            prob = random.random()
            if prob <= 0.4:
                self.cur1 = simulation.first_computer()
                prob = random.random()
                self.fst_count.__add__(1)

                if prob <= 0.3:
                    self.cur2 = simulation.second_computer()
                    que.pop()
                    self.snd_count.__add__(1)

                else:
                    self.cur2 = simulation.third_computer()
                    que.pop()
                    self.trd_count.__add__(1)

            elif prob > 0.7:
                self.cur1 = simulation.third_computer()
                que.pop()
                self.trd_count.__add__(1)

            else:
                self.cur1 = simulation.second_computer()
                que.pop()
                self.snd_count.__add__(1)

            self.all = time_generate.sum_date([str(self.all),
                                               str(time_generate.sum_date([str(self.cur1), str(self.cur2)]))])

        return self.all, self.fst_count, self.snd_count, self.trd_count

    def interface(self):
        # tasks = int(input("Количество деталей: "))
        print(self.time_counter(tasks=200))


if __name__ == '__main__':
    # d1 = datetime.strptime('00:00:00', '%H:%M:%S')
    # d2 = datetime.strptime('00:01:00', '%H:%M:%S')
    # print(time_generate.random_date(d1, d2))
    GG = simulation()
    GG.interface()
