'''
    This problem is Minesweeper.
    
    https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=13&page=show_problem&problem=1130
'''


times = 1
    
while True:
    M, N = map(int, input().split())
    
    if M == 0 and N == 0:
        break
    matrix = []
    for i in range(M):
        s = ' '.join(input()).split()
        for i in range(N):
            if s[i] == '.':
                s[i] = 0
        matrix.append(s)
        
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == '*':
                pass
            else:
                s = 0
                if i - 1 >= 0 and j - 1 >= 0:
                    s += int(matrix[i-1][j-1] == '*')
                if i - 1 >= 0:
                    s += int( matrix[i-1][j] == '*')
                if i - 1 >= 0 and j + 1 < N:
                    s += int( matrix[i-1][j+1] == '*')
                if j - 1 >= 0:
                    s += int( matrix[i][j-1] == '*')
                if j + 1 < N:
                    s += int( matrix[i][j+1] == '*')
                if i + 1 < M and j - 1 >= 0:
                    s += int( matrix[i+1][j-1] == '*')
                if i + 1 < M:
                    s += int( matrix[i+1][j] == '*')
                if i + 1 < M and j + 1 < N:
                    s += int( matrix[i+1][j+1] == '*')
                
                matrix[i][j] = str(s)
    if times == 1:
        print(f'Field #{times}:')
    else:
        print(f'\nField #{times}:')
    for rows in matrix:
        print(''.join(rows))
        
    times += 1