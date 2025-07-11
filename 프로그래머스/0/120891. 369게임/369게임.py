def solution(order):
    answer = 0
    num = ["3", "6", "9"]
    
    order = str(order)
    
    for i in order:
        if i in num:
            answer += 1
    
    return answer