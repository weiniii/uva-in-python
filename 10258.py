'''
    This problem is Contest Scoreboard.
    
    https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=14&page=show_problem&problem=1199
'''


counts = int(input())
pas = input()
for i in range(counts):
    time = {}
    correct = {}
    uncorrect = {}
    times = {}
    while True:
        try:
            inputs = input().split()
            inputs[:-1] = list(map(int, inputs[:-1]))
        except:
            break
        if len(inputs) == 0:
            break
        if inputs[0] not in time.keys():
            if inputs[3] == 'C':
                time.setdefault(inputs[0], int(inputs[2]))
                correct.setdefault(inputs[0], [inputs[1]])
                uncorrect.setdefault(inputs[0], [])
                times.setdefault(inputs[0], 1)
            elif inputs[3] == 'I':
                time.setdefault(inputs[0], 0)
                correct.setdefault(inputs[0], [])
                uncorrect.setdefault(inputs[0], [inputs[1]])
                times.setdefault(inputs[0], 0)
            else:
                time.setdefault(inputs[0], 0)
                correct.setdefault(inputs[0], [])
                uncorrect.setdefault(inputs[0], [])
                times.setdefault(inputs[0], 0)
        else:
            if inputs[3] == 'C':
                if inputs[1] in correct[inputs[0]]:
                    pass
                else:
                    time[inputs[0]] += int(inputs[2])
                    correct[inputs[0]].append(inputs[1])
                    times[inputs[0]] += 1
            elif inputs[3] == 'I':
                if inputs[1] in correct[inputs[0]]:
                    pass
                else:
                    uncorrect[inputs[0]].append(inputs[1])
    times = dict(sorted(times.items(), key=lambda item: item[0]))
    times = dict(sorted(times.items(), key=lambda item: item[1], reverse=True))
    ind = 0
    new_times = {}
    while ind < len(list(times.values())):
        pk = list(times.values())[ind]
        candidate = sum([1 if pk == list(times.values())[j] else 0 for j in range(len(times.values()))])
        their_time = [time[list(times.keys())[player]] + sum([20 if answer in correct[list(times.keys())[player]] else 0 for answer in uncorrect[list(times.keys())[player]]]) for player in range(ind, ind + candidate)]
        for new in sorted(range(len(their_time)), key=lambda k: their_time[k]):
            new_times.setdefault(list(times.keys())[new + ind], list(times.values())[new + ind])
        ind += candidate
    for player in new_times.keys():
        if player == list(times.keys())[-1] and i != counts-1:
            print(f'{player} {len(correct[player])} {time[player] + sum([20 if answer in correct[player] else 0 for answer in uncorrect[player]])}\n')
        else:
            print(f'{player} {len(correct[player])} {time[player] + sum([20 if answer in correct[player] else 0 for answer in uncorrect[player]])}')