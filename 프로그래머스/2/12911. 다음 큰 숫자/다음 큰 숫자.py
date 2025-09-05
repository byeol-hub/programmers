def solution(n):
    answer = 0
    count = bin(n)[2:].count("1")
    
    for i in range(n+1, 1000001):
        count_n = bin(i)[2:].count("1")
        if count == count_n:
            answer = i
            break
    
    return answer