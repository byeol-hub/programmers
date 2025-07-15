def solution(numbers):
    answer = 0
    arr =[]
    
    numbers.sort()
        
    arr.append(numbers[0]*numbers[1])
    arr.append(numbers[-1]*numbers[-2])
    answer = max(arr)
        
    
    return answer