def solution(emergency):
    answer = []
    emergency_sort = []
    
    emergency_sort = sorted(emergency, reverse=True)
    
    for i in range(len(emergency)):
        answer.append(emergency_sort.index(emergency[i])+1)
    
    return answer

















# def solution(emergency):
#     answer = []
#     answer = emergency.copy()
#     arr = emergency.copy()
    
#     arr.sort(reverse=True)
    
#     for i in range(len(emergency)):
#         answer[i] = arr.index(emergency[i]) + 1
    
#     return answer