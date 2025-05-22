def solution(arr, queries):
    answer = []
    result = []
    for query in queries:
        result = [i for i in arr[query[0]:query[1]+1] if i > query[2]]
        if result != []:
            min_result = min(result)
            answer.append(min_result)
        else:
            answer.append(-1)
    return answer

# def solution(arr, queries):
#     answer = []
#     result = []
#     query = []
#     for query in queries:
#         for i in query:
#             result = [i for i in arr[query[0]:query[1]+1] if i > query[2]]
            
#             if result != []:
#                 min_result = min(result)
#                 answer.append(min_result)
                
#                 for j in result:
#                     answer += min(result)
                    
#             else:
#                 answer.append(-1)
#     return answer

