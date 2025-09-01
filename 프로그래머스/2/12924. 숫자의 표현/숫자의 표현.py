def solution(n):
    answer = 0
    i = 0
    
    while i < n:
        sum = 0
        i += 1
        for j in range(i, n+1):
            sum += j
            if sum == n:
                answer += 1
            elif sum > n:
                break
        
    
    return answer