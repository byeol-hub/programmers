def solution(arr):
    answer = []
    a = []
    for i in range(len(arr)):
        if arr[i] == 2:
            a.append(i)
            
    if a == []:
        answer.append(-1)
    else: 
        answer = arr[a[0]:a[-1]+1]
        
    return answer