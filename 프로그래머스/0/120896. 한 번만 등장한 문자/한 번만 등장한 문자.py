# def solution(s):
#     answer = ''
#     s_unique = list(set(s))
#     s_count = []
#     answer_arr = []
    
#     for i in range(len(s_unique)):
#         s_count.append(0)

#     for i in range(len(s_unique)):
#         for j in s:
#             if s_unique[i] == j:
#                 s_count[i] += 1
    
#     for i in range(len(s_count)):
#         if s_count[i] == 1:
#             answer_arr.append(s_unique[i])
    
#     answer_arr.sort()
    
#     for i in answer_arr:
#         answer += i
    
#     return answer


def solution(s):
    answer = ''
    s_set = list(set(s))
    s_set.sort()
    
    for i in s_set:
        if s.count(i) == 1:
            answer += i
    
    return answer