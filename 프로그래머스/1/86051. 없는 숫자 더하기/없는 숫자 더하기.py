def solution(numbers):
    answer = 0
    
    num = [0,1,2,3,4,5,6,7,8,9]
    
    for i in numbers:
        if i in num:
            num.remove(i)
    
    for i in num:
        answer += i
    
    return answer