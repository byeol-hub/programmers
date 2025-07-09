def solution(balls, share):
    answer = 1
    num_1 = 1
    num_2 = 1
    
    for i in range(balls, 0, -1):
        answer *= i
        
    for i in range(balls-share, 0, -1):
        num_1 *= i
    
    for i in range(share, 0, -1):
        num_2 *= i
    
    answer = answer / (num_1*num_2) 
    
    return answer