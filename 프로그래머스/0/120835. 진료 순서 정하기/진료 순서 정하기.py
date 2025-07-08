def solution(emergency):
    answer = []
    answer = emergency.copy()
    arr = emergency.copy()
    
    arr.sort(reverse=True)
    
    for i in range(len(emergency)):
        answer[i] = arr.index(emergency[i]) + 1
    
    return answer