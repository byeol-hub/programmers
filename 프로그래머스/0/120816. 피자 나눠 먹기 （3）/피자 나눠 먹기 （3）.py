def solution(slice, n):
    answer = 0
    
    for i in range(1, 51):
        if i*slice - n >= 0:
            answer = i
            break
    
    return answer