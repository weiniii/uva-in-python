'''
    This problem is Maximum Product.
    
    https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2000
'''


def get_product(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return max(arr[0], 0)
    elif len(arr) == 2:
        return max(arr[0]*arr[1], arr[0], arr[1], 0)
    else:
        product = 1
        for i, p in enumerate(arr):
            if p == 0:
                return max(get_product(arr[:i]), get_product(arr[i+1:]), 0)
            else:
                product *= p

        if product > 0 :
            return product
        else:
            for i, p in enumerate(arr):
                if p < 0:
                    break
            for j in range(len(arr) - 1, -1, -1):
                if arr[j] < 0:
                    break
            if i == j:
                return max(get_product(arr[:i]), get_product(arr[i+1:]), 0)
            else:
                return max(get_product(arr[:i]), get_product(arr[i+1:]), get_product(arr[:j]), get_product(arr[j+1:]), 0)

times = 1
  
while True:
    try:
        number = int(input())
        input_list = input().split()
        numbers = [int(input_list[i]) for i in range(len(input_list))]
        max_number = get_product(numbers)
        print(f'Case #{times}: The maximum product is {max_number}.')
         
        pas = input()
        print('')
        times += 1
    except EOFError:
        break

print('')