'''
    This problem is Zeros and Ones.
    
    https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1265
'''


cases = 0

while True:
    try:
        inputs = input()
    
        if not len(inputs):
            break
        cases += 1
        print(f'Case {cases}:')
        
        value = int(inputs[0])
        inputs_cum = [value]
        
        for i in range(1, len(inputs)):
            value += int(inputs[i])
            inputs_cum.append(value)
        
        counts = int(input())    
        
        for i in range(counts):
            
            left, right = map(int, input().split())
            
            left, right = min(left, right), min(max(left, right), len(inputs) - 1)
                
            if ((inputs_cum[right] == inputs_cum[left] and inputs[left] == '0') or
                (inputs_cum[right] - inputs_cum[left] == right - left and inputs[left] == '1')):
                print('Yes')
            else:
                print('No')
        
    except (EOFError):
        break