import random

from collections import deque
from datetime import timedelta, datetime
from config import task_list


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
        self.fst_complete_count, self.snd_complete_count, self.trd_complete_count = 0, 0, 0
        self.cur1, self.cur2, self.total_time = timedelta(), timedelta(), timedelta(hours=0, minutes=0, seconds=0)
        self.num_tasks = int(task_list[0])
        self.evm_count = 3
        self.evm_queues = [[], [], []]  # очереди заданий для каждой ЭВМ
        self.evm_times = [0, 0, 0]  # время завершения обработки задания на каждой ЭВМ
        self.comp_times = []  # время обработки каждого задания

        # вероятности направления задания на каждую ЭВМ:
        self.evm_probs = [float(task_list[1]),
                          float(task_list[2]),
                          1 - (float(task_list[1]) + float(task_list[2]))]

        # вероятности направления задания после обработки на каждой ЭВМ:
        self.comp_probs = [[0.7, 0.3, 0], [0.3, 0.7, 0], [0, 0, 1]]

        self.evm_durations = [[4, 1], [3, 1], [5, 2]]  # интервалы времени обработки задания на каждой ЭВМ
        self.repeat_count = int(task_list[6]) # Количество повторений задания

    def time_counter(self, tasks=int(task_list[0])):
        # task_list = [task_count, p1st, p2nd, p2nd_after, interval1, interval2, repeat_count]

        for i in range(self.num_tasks):
            # генерация задания
            prob = random.random()

            if prob < self.evm_probs[0]:
                self.evm_queues[0].append(i)
            elif prob < self.evm_probs[0] + self.evm_probs[1]:
                self.evm_queues[1].append(i)
            else:
                self.evm_queues[2].append(i)

            # проверка очередей и обработка заданий
            for j in range(self.evm_count):
                if self.evm_queues[j]:
                    if self.evm_times[j] <= i:
                        task_id = self.evm_queues[j].pop(0)
                        duration = random.randint(self.evm_durations[j][0] - self.evm_durations[j][1],
                                                  self.evm_durations[j][0] + self.evm_durations[j][1])
                        self.comp_times.append(i + duration)

                        if j == 0:
                            prob = random.random()
                            if prob < self.comp_probs[0][0]:
                                self.evm_queues[1].append(task_id)
                            elif prob < self.comp_probs[0][0] + self.comp_probs[0][1]:
                                self.evm_queues[2].append(task_id)

                        elif j == 1:
                            prob = random.random()
                            if prob < self.comp_probs[1][0]:
                                self.evm_queues[0].append(task_id)
                            elif prob < self.comp_probs[1][0] + self.comp_probs[1][1]:
                                self.evm_queues[2].append(task_id)
                        else:
                            pass
                        self.evm_times[j] = i + duration

        # вывод результатов моделирования
        print("Обработано заданий:", len(self.comp_times))
        print("Среднее время обработки одного задания:", sum(self.comp_times) / len(self.comp_times), "минут")
        print("Максимальное время ожидания в очереди на первой ЭВМ:",
              max([self.evm_times[0] - i for i in self.evm_queues[0]]), "минут")

        return self.total_time, [self.fst_complete_count, self.snd_complete_count, self.trd_complete_count]


if __name__ == '__main__':
    GG = simulation()
    GG.time_counter()
