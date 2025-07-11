# def solution(sides):
#     answer = 0
    
#     sides.sort()
    
#     for i in range(sides[1], sides[0] + sides[1]): # 가장 긴 변일 때
#         answer += 1
        
#     for i in range(1, sides[1]): # 가장 긴 변이 아닐 때
#         if i+sides[0] > sides[1]:
#             answer += 1
#         else:
#             continue
        
#     return answer


def solution(sides):
    answer = 0
    
    sides.sort()
    
    answer= sides[0] + abs(-sides[0] + 1)
    
    return answer