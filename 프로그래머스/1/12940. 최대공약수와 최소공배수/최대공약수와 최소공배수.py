def solution(n, m):
    import math

    answer = [math.gcd(n,m)]
    answer.append(n*m//answer[0])
    
    return answer