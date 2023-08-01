'''
    This problem is Is This Integration ?
    
    https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=14&page=show_problem&problem=1150
'''


import math

while True:
    try:
        r = float(input())
        A = r * r * math.pi / 6 - math.sqrt(3) * r * r / 4
        B = r * r * math.pi / 12 - A
        C = r * r - r * r * math.pi / 4 - B
        D = B - C
        C = 4 * C
        D = 4 * D
        E = r * r - C - D
        print(f'{E:.3f} {D:.3f} {C:.3f}')
    except:
        break