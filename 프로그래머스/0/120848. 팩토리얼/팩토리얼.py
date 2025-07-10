def solution(n):
    answer = 0
    
    for i in range(1, 12):
        n /= i
        if n < 1.0:
            answer = i - 1
            break
    
    return answer