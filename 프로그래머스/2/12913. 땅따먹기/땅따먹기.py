# def solution(land):
#     answer = 0
#     now_max_value = 0
#     next_max_value = 0
#     index = 0
    
#     for i in range(len(land)-1):
#         if land[i].index(max(land[i])) != land[i+1].index(max(land[i+1])):
#             answer += max(land[i])
#             if i == len(land)-2:
#                 answer += max(land[i+1])
#         else:
#             next_max_value = max(land[i+1])
#             now_max_value = max(land[i])
#             index = land[i].index(max(land[i]))
            
#             land[i+1][index] = 0
#             land[i][index] = 0
            
#             if now_max_value + max(land[i+1]) < max(land[i]) + next_max_value:
#                 land[i+1][index] = next_max_value
#                 answer += max(land[i])
#                 if i == len(land)-2:
#                     answer += next_max_value
            
#             elif now_max_value + max(land[i+1]) == max(land[i]) + next_max_value:
#                 if i == len(land)-2:
#                     answer += now_max_value + max(land[i+1])
#                 else:
#                     if land[i+2].index(max(land[i+2])) == index:
#                         answer += now_max_value
#                     elif land[i+2].index(max(land[i+2])) == land[i+1].index(max(land[i+1])):
#                         land[i+1][index] = next_max_value
#                         answer += max(land[i])
                    
#             else:
#                 answer += now_max_value
#                 if i == len(land)-2:
#                     answer += max(land[i+1])
                
#     return answer

def solution(land):
    answer = 0
    
    for i in range(1, len(land)):
        for j in range(4):
            if j != land[i-1].index(max(land[i-1])):
                land[i][j] += max(land[i-1])
            else:
                land[i][j] += max(sorted(land[i-1])[:-1])
    
    answer = max(land[len(land)-1])

    return answer


