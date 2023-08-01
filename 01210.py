'''
    This problem is Sum of Consecutive Prime Numbers.

    https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3651
'''


prime = [2, 3]
while True:
    num = int(input())
    if num == 0:
        break
    elif num == 2 or num == 3:
        print(1)
        continue
    elif prime[-1] > num:
        pass
    else:
        for i in range(prime[-1], num + 1, 2):
            IS = 1
            for p in prime:
                if i % p == 0:
                    IS = 0
                    break
            if IS:
                prime.append(i)

    i = 0
    j = 1
    counts = 0
    while True:
        if sum(prime[i:j]) < num:
            j += 1
        elif sum(prime[i:j]) == num:
            counts += 1
            i += 1
        else:
            i += 1
        if len(prime) < j or len(prime) < i:
            break
    print(counts)