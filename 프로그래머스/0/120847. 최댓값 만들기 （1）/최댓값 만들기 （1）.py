def solution(numbers):
    answer = 0
    
    numbers.sort(reverse=True)
    
    answer = numbers[0]*numbers[1]
    
    return answer


















# def solution(numbers):
#     answer = 1
    
#     answer *= max(numbers)
    
#     numbers.remove(max(numbers))
    
#     answer *= max(numbers)
    
#     return answer