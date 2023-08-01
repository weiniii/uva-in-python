'''
    This problem is last digit.
    
    https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=13&page=show_problem&problem=1103
'''


while True:
    N = int(input())
    sub = [1, 4, 7, 6, 5, 6, 3, 6, 9, 0, 1, 6, 3, 6, 5, 6, 7, 4, 9, 0]
    if N == 0:
        break
    else:
        Q = N // 20
        R = N % 20
        total = Q * 14
        for i in range(R):
            total += sub[i]
        print(total % 10)