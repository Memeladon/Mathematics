import random

# ввод исходных данных
num_tasks = 200
evm_count = 3
evm_queues = [[], [], []]  # очереди заданий для каждой ЭВМ
evm_times = [0, 0, 0]  # время завершения обработки задания на каждой ЭВМ
comp_times = []  # время обработки каждого задания
evm_probs = [0.4, 0.3, 0.3]  # вероятности направления задания на каждую ЭВМ
comp_probs = [[0.7, 0.3, 0], [0.3, 0.7, 0], [0, 0, 1]]  # вероятности направления задания после обработки на каждой ЭВМ
evm_durations = [[4, 1], [3, 1], [5, 2]]  # интервалы времени обработки задания на каждой ЭВМ

# имитационное моделирование
for i in range(num_tasks):
    # генерация задания
    prob = random.random()
    if prob < evm_probs[0]:
        evm_queues[0].append(i)
    elif prob < evm_probs[0] + evm_probs[1]:
        evm_queues[1].append(i)
    else:
        evm_queues[2].append(i)

    # проверка очередей и обработка заданий
    for j in range(evm_count):
        if evm_queues[j]:
            if evm_times[j] <= i:
                task_id = evm_queues[j].pop(0)
                duration = random.randint(evm_durations[j][0] - evm_durations[j][1], evm_durations[j][0] + evm_durations[j][1])
                comp_times.append(i + duration)
                if j == 0:
                    prob = random.random()
                    if prob < comp_probs[0][0]:
                        evm_queues[1].append(task_id)
                    elif prob < comp_probs[0][0] + comp_probs[0][1]:
                        evm_queues[2].append(task_id)
                elif j == 1:
                    prob = random.random()
                    if prob < comp_probs[1][0]:
                        evm_queues[0].append(task_id)
                    elif prob < comp_probs[1][0] + comp_probs[1][1]:
                        evm_queues[2].append(task_id)
                else:
                    pass
                evm_times[j] = i + duration

# вывод результатов моделирования
print("Обработано заданий:", len(comp_times))
print("Среднее время обработки одного задания:", sum(comp_times) / len(comp_times), "минут")
print("Максимальное время ожидания в очереди на первой ЭВМ:", max([evm_times[0] - i for i in evm_queues[0]]), "минут")
#
# que = deque([i for i in range(tasks)])  # Очередь всех заданий
#
#         while len(que) != 0:
#             prob = random.random()
#             if prob <= float(task_list[1]):
#                 self.first.append(que[0])
#                 que.popleft()
#                 self.cur1 = simulation.first_computer()
#                 prob = random.random()
#                 self.fst_complete_count += 1
#
#                 if prob <= float(task_list[3]):
#                     self.cur2 = simulation.second_computer()
#
#                     self.second.append(self.first[0])
#                     self.first.popleft()
#
#                     self.snd_complete_count += 1
#
#                 else:
#                     self.cur2 = simulation.third_computer()
#                     que.pop()
#                     self.trd_complete_count += 1
#
#             elif prob > float(task_list[2]):
#                 self.cur1 = simulation.third_computer()
#                 que.pop()
#                 self.trd_complete_count += 1
#
#             else:
#                 self.cur1 = simulation.second_computer()
#                 que.pop()
#                 self.snd_complete_count += 1
#
#             self.total_time = time_generate.sum_date([str(self.total_time),
#                                                       str(time_generate.sum_date([str(self.cur1), str(self.cur2)]))])
