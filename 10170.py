'''
    This problem is The Hotel with Infinite Rooms.
    
    https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=13&page=show_problem&problem=1111
'''


while True:
    try:
        S, D = map(int, input().split())
        result = (((1 - 4 * (- 2 * D - S * S + S) )** 0.5) - 1) / 2
        if result % 1 != 0:
            print(int(result + 1))
        else:
            print(int(result))
    except:
        break