def solution(s):
    answer = True
    p_num = 0
    y_num = 0
    
    for i in s:
        num = i.lower()
        if  num == 'p':
            p_num += 1
        elif num == 'y':
            y_num += 1
    
    if p_num != y_num:
        answer = False

    return answer