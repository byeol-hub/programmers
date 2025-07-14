def solution(n):
    answer = 2
    
    import math
    
    if int(math.sqrt(n))**2 == n:
        answer = 1
    
    return answer