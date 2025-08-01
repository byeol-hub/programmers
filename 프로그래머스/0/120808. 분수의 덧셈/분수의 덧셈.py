# def solution(numer1, denom1, numer2, denom2):
#     answer = []
#     sum_arr = []
#     denom1_arr = []
#     denom_arr = []
#     sum = 0
    
#     numer1 *= denom2
#     numer2 *= denom1
    
#     denom1 *= denom2
    
#     sum = numer1 + numer2
    
#     for i in range(2, sum+1):
#         if sum % i == 0:
#             sum_arr.append(i)
            
#     for i in range(2, denom1+1):
#         if denom1 % i == 0:
#             denom1_arr.append(i)
                
#     if len(sum_arr) >= len(denom1_arr):
#         for i in range(len(denom1_arr)):
#             if denom1_arr[i] in sum_arr:
#                 denom_arr.append(denom1_arr[i])
#     else:
#         for i in range(len(sum_arr)):
#             if sum_arr[i] in denom1_arr:
#                 denom_arr.append(sum_arr[i])
    
#     denom_arr.sort(reverse = True)
    
#     for i in denom_arr:
#         if sum // i == 0 or denom1 // i == 0:
#             print(sum, denom1, denom_arr)
#             break
#         else:
#             sum //= i
#             denom1 //= i
        
#     answer = [sum, denom1]
    
#     return answer


def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    min_num = min(numer, denom)
    result = 0
    
    for i in range(min_num, 0, -1):
        if numer % i == 0 and denom % i == 0:
            result = i
            break

    # 기약분수로 나누기
    numer //= result
    denom //= result

    return [numer, denom]

