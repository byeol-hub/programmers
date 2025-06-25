def solution(num):
    answer = 0
    count = 0
    
    if num == 1:
        return answer
    
    while (num > 1):
        if num % 2 == 0:
            num /= 2
            count += 1
        else:
            num = num*3 + 1
            count += 1
        if count > 500:
            answer = -1
            return answer
            
    answer = count
    
    return answer