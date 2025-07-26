def solution(a, b):
    answer = 0
    a_arr = []
    b_arr = []
    a_b = 1
    
    # a의 약수
    for i in range(2, a+1): 
        if a % i == 0:
            a_arr.append(i)
            
    # b의 약수
    for i in range(2, b+1):
        if b % i == 0:
            b_arr.append(i)

    # a와 b의 공통 약수
    for i in a_arr[::-1]:
        if i in b_arr:
            a_b = i
            break
    
    b //= a_b     
    
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
        
    if b == 1:
        answer = 1
    else:
        answer = 2
    
    return answer


# def solution(a, b):
#     answer = 1
#     a_arr = []
#     b_arr = []
#     a_b = []
#     result = []
#     result_b = []
    
#     # a의 약수
#     for i in range(2, a+1): 
#         if a % i == 0:
#             a_arr.append(i)
            
#     # b의 약수
#     for i in range(2, b+1):
#         if b % i == 0:
#             b_arr.append(i)

#     # a와 b의 공통 약수
#     for i in a_arr[::-1]:
#         if i in b_arr:
#             a_b.append(i)
    
#     # a와 b를 각각 a와 b의 공약수로 나눔
#     while (len(a_b) != 0):
#         if a // a_b[-1] != 0:
#             a //= a_b[-1]
#             b //= a_b[-1]
#             a_b.pop()
#         else:
#             break
        
#     # 기약분수의 분모(b)의 약수
#     for i in range(2, b+1):
#         if b % i == 0:
#             result.append(i)
            
#     result_b = result.copy()
    
#     # 기약분수의 분모(b)의 소인수 -> 1과 자기자신 외의 약수 x
#     for i in result:
#         for j in range(2,i):
#             if i % j == 0:
#                 result_b.remove(i)
#                 break
    
#     # 기약분수의 분모(b)의 소인수 중에서 2도 아니고 5도 아닌 수가 있다면 2를 반환
#     for i in result_b:
#         if i != 2 and i != 5:
#             answer = 2
#             return answer
    
#     return answer


