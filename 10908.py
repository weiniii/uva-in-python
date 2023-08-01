'''
    This problem is Largest Square.

    https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1849
'''


counts = int(input())

for r1 in range(counts):
    M, N, Q = map(int, input().split())
    farm = []
    for r2 in range(M):
        farm.append(input()[:N])
    print(f'{M} {N} {Q}')
    for r3 in range(Q):
        i, j = map(int, input().split())
        center = farm[i][j]
        
        r = 0
        IF = 1
        while True:
            r += 1
            i1, j1, i2, j2 = i - r, j - r, i + r, j + r
            if i2 >= M or i1 < 0 or j1 < 0 or j2 >= N:
                r -= 1
                break
            for r4 in range(j1, j2 + 1):
                if farm[i1][r4] != center:
                    IF = 0
                    break
                if farm[i2][r4] != center:
                    IF = 0
                    break
            if IF:
                for r5 in range(i1, i2 + 1):
                    if farm[r5][j1] != center:
                        IF = 0
                        break
                    if farm[r5][j2] != center:
                        IF = 0
                        break
            else:
                r -= 1
                break

            if IF == 0:
                r -= 1
                break
            
        print(f'{r * 2 + 1}')