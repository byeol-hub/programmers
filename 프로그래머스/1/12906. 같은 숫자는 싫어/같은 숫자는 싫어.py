# def solution(arr):
#     answer = []
#     temp = 10
#     n = 0
        
#     for i in range(len(arr)):
#         temp = arr[i]
#         while(temp == arr[i]):
#             n += 1
#             if i + n > len(arr):
#                 break
#             else:
#                 temp = arr[i+n]
#         answer.append(arr[i+n])
        
#     return answer

def solution(arr):
    answer = []
    result = []
    result.append(arr[0])
    answer.append(arr[0])
    
    for i in range(len(arr)-1):
        result.append(arr[i+1])
        answer.append(arr[i+1])
        if result[i] == result[i+1]:
            answer.pop()
            
    return answer


