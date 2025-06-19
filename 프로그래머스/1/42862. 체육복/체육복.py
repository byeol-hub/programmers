def solution(n, lost, reserve):
    answer = 0
    arr = []
    lost.sort()
    reserve.sort()
    answer = n - len(lost) 
    
    for i in lost:
        if i in reserve:
            arr.append(i)
            answer += 1
    
    for i in arr:
        lost.remove(i)
        reserve.remove(i)
            
    for i in lost:
        if i-1 in reserve:
            answer += 1
        elif i+1 in reserve:
            answer += 1
            reserve.remove(i+1)
    return answer
