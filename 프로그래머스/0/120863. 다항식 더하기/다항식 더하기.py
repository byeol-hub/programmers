def solution(polynomial):
    answer = ''
    now = ''
    num = 0
    num_str = 0
    num_str_arr = []
    arr = []
    arr = polynomial.split('+')
    
    print(arr)
    
    for i in arr:
        now = i.strip()
        if 'x' in now:
            if now[0:len(now)-1] == '':
                num_str += 1
                print(now, num_str)
            else:
                num_str += int(now[0:len(now)-1])
                print(now, num_str)
        else:
            num += int(now)
            
    print(num_str, num)
    
    if num == 0:
        if num_str == 0:
            answer = ''
        elif num_str == 1:
            answer = 'x'
        else:
            answer = str(num_str)+'x'
    elif num_str == 1:
        answer = 'x'+' + '+str(num)
    elif num_str == 0:
        answer = str(num)
    else:
        answer = str(num_str)+'x'+' + '+str(num)
    
    return answer