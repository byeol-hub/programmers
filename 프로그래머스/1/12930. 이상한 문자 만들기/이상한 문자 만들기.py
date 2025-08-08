def solution(s):
    answer = ''
    s_arr = []
    
    s_arr = s.split(' ')
    print(s_arr)
    
    for i in s_arr:
        answer += ' '
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
    
    answer = answer[1:]
    
    return answer