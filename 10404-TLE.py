'''
    This problem is Bachet's Game.

    https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1345
'''


while True:
    try:
        N, M, *choose = map(int, input().split())
    except EOFError:
        break
    
    wins = [False] * (N + 1)
    for i in range(1, N + 1):
        for action in choose:
            if i >= action and not wins[i - action]:
                wins[i] = True
                break
    if wins[N]:
        print('Stan wins')
    else:
        print('Ollie wins')