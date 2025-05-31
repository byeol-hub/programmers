def solution(my_string, indices):
    answer = ''
    arr = []
    n = 0
    
    for i in my_string:
        arr.append(i)
    
    print(arr)
        
    for i in indices:
        arr[i] = '0'
        n += 1
    
    for i in range(n):
        if '0' in arr:
            arr.remove('0')
    
    for i in arr:
        answer += i
            
    return answer