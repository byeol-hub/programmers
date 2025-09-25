def solution(progresses, speeds):
    day = []
    
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            day.append((100 - progresses[i]) // speeds[i])
        else:
            day.append(((100 - progresses[i]) // speeds[i])+1)
    
    answer = [1]
    value = day[0]
    
    for i in day[1:]:
        if value >= i:
            answer[-1] += 1
        else:
            value = i
            answer.append(1)
    
    return answer