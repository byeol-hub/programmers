def solution(chicken):
    answer = 0
    c_chicken = 0
    
    answer += chicken // 10
    c_chicken = (chicken // 10) + (chicken % 10)
    
    while (c_chicken // 10 != 0):
        answer += c_chicken // 10
        c_chicken = (c_chicken // 10) + (c_chicken % 10)
    
    return answer