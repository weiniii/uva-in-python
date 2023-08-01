'''
    This problem is Brick Wall Patterns.
    
    https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=11&page=show_problem&problem=841
'''


def F(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    elif n == 4:
        return 5
    elif n == 5:
        return 8
    else:
        return 3 * F(n-5) + 5 * F(n-4)

while True:
    num = int(input())
    if num == 0:
        break
    else:
        print(F(num))