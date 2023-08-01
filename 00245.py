'''
    This problem is Uncompress.

    https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=181
'''


dic = []
while True:
    inputs = input()
    if inputs == '0':
        break
    i = 0
    s = ''
    word = ''
    length = len(inputs)
    while i < length:
        if ('a' <= inputs[i] and inputs[i] <= 'z') or ('A' <= inputs[i] and inputs[i] <= 'Z'):
            word += inputs[i]
        elif word != '':
            try:
                dic.remove(word)
                dic.append(word)
                word = ''
            except:
                dic.append(word)
                word = ''
        else:
            pass
        
        s += inputs[i]
        
        if '0' <= inputs[i] and inputs[i] <= '9':
            c = 1
            while True:
                try:
                    out = int(inputs[i:i+c])
                    c += 1
                    if i + c > length:
                        break
                except:
                    c -= 1 
                    break
                
            i += len(str(out))
            updata_word = dic[-out]
            s = s[:-1] + updata_word
            dic.pop(-out)
            dic.append(updata_word)
        else:
            i += 1
    if word !=  '':
        try:
            dic.remove(word)
            dic.append(word)
        except:
            dic.append(word)
    print(s)