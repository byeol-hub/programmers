def solution(common):
    answer = 0
    common_m = []
    common_x = []
    
    for i in range(len(common)-1):
        if common[i] == 0:
            common_m.append(common[i+1] - common[i])
            answer = common[-1] + common_m[0]
            return answer
        common_m.append(common[i+1] - common[i])
        common_x.append(int(common[i+1] / common[i]))
    
    if len(set(common_m)) == 1: # 등차수열
        answer = common[-1] + common_m[0]
    else: 
        answer = common[-1] * common_x[0]
    
    return answer


# def solution(common):
#     answer = 0
#     common_m = []
#     common_x = []
    
#     for i in range(len(common)-1):
#         common_m.append(common[i+1] - common[i])
#         common_x.append(int(common[i+1] / common[i]))
#         if len(set(common_m)) > 1:
#             answer = 1
#             break
#         if len(set(common_x)) > 1:
#             answer = 2
#             break
    
#     if answer == 2: # 등차수열
#         answer = common[-1] + common_m[0]
#     else: 
#         answer = common[-1] * common_x[0]
    
#     return answer