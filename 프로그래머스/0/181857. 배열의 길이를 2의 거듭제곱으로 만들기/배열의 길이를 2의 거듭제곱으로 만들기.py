# def solution(arr):
#     answer = []
#     a = len(arr)
#     n = 0 
    
#     for i in range(1, 11, 1):
#         if a == 2**i:
#             answer = arr
#             break
            
#         else:
#             for j in range(1000):
#                 a += 1
#                 n += 1
#                 for y in range(1, 11, 1):
#                     if a == 2**y:
#                         print(2**y)
#                         print(n)
#                         break
#                 break
            
#     for z in range(n):
#         arr.append(0)
#     answer = arr
        
#     return answer

def solution(arr):
    answer = []
    a = len(arr) - 1
    n = -1
    b = 0
            
    for j in range(1000):
        a += 1
        n += 1
        
        for y in range(1, 11, 1):
            if a == 2**y:
                b = y
                break
                
        if a == 2**b:
            break
            
    for z in range(n):
        arr.append(0)
    answer = arr
        
    return answer

