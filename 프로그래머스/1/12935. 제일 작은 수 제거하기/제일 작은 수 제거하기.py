def solution(arr):
    answer = []
    arr_min = 0
    
    if len(arr) > 1: 
        arr_min = min(arr)
        arr.remove(arr_min)
        answer = arr
    else:
        answer.append(-1)
    
    return answer