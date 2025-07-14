def solution(my_string):
    answer = ''
    arr = []
    
    answer = my_string.lower()
    
    for i in answer:
        arr.append(i)
        
    arr.sort()
    answer = ''
    
    for i in arr:
        answer += i
    
    return answer