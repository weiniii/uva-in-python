'''
    This problem is Robot Instructions.
    
    https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=441&page=show_problem&problem=3947
'''


counts = int(input())
for i in range(counts):
    num = int(input())
    s = []
    for j in range(num):
        intro = input()
        if intro == 'LEFT':
            s.append(-1)
        elif intro == 'RIGHT':
            s.append(1)
        else:
            ind = int(intro.split()[-1])
            s.append(s[ind - 1])
    print(sum(s))