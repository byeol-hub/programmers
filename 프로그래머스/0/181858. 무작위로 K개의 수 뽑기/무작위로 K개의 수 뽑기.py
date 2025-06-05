# def solution(arr, k):
#     answer = []
#     arr = set(arr)
#     for i in arr:
#         answer.append(i)
#         if len(answer) >= k:
#             break
            
#     if len(answer) < k:
#         for i in range(k-len(answer)):
#             answer.append(-1)
#     return answer

def solution(arr, k):
    answer = []
    
    for i in arr:
        if i not in answer:
            answer.append(i)
        if len(answer) == k:
            break
            
    if len(answer) < k:
        for i in range(k-len(answer)):
            answer.append(-1)
            
    return answer