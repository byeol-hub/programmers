# def solution(n):
#     answer = []
#     for i in range(n+1):
#         if i % 2 == 0:
#             answer = i / 2
#         else:
#             answer = 3*i + 1
        
#     return answer

def solution(n):
    answer = []
    answer.append(n)
    while (n != 1):
        if n % 2 == 0:
            n = n/2
            answer.append(n)
            
        else:
            n = 3*n+1
            answer.append(n)
            
    return answer




