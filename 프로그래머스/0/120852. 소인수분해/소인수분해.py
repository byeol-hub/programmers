def solution(n):
    answer = []
    arr = []
    array = []
    
    for i in range(2, n+1):
        if n % i == 0:
            arr.append(i)
    
    for i in arr:
        for j in range(2, i):
            if i % j == 0:
                array.append(i)            
    
    array = list(set(array))
    
    for i in arr:
        if i not in array:
            answer.append(i)
    
    answer.sort()
    
    return answer