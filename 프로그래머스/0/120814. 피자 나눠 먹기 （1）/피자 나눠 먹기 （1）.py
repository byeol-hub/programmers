def solution(n):
    answer = 0
    
    all = n // 7
    some = n % 7
    
    if some == 0:
        answer = all
    else:
        answer = all + 1
    
    return answer