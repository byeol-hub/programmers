def solution(food):
    answer = ''
    answer_reverse = ''
    
    for i in range(len(food)):
        if food[i] < 2:
            continue
        else:
            food[i] = food[i]//2
            for j in range(food[i]):
                answer += str(i)
    
    for i in range(len(answer)):
        answer_reverse += answer[-i-1]
    
    answer += '0'+ answer_reverse
    
    return answer