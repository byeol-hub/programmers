# def solution(number, k):
#     next_k = k
    
#     # number에서 수를 하나씩 삭제해가며, 총 k개를 삭제하는데 이때 현재의 값이 현재 상황에서 최대값이 되도록 삭제하기
#     while next_k != 0:
#         k = next_k
#         for i in range(len(number)-1):
#             if number[i] < number[i+1]:
#                 number = number[:i] + number[i+1:]
#                 next_k -= 1
#                 break
#         if k == next_k:
#             number = number[:-k]
#             break
     
#     return number

# stack 사용
def solution(number, k):
    number_stack = []
    for i in number:
        while (k > 0) and (number_stack != []) and (number_stack[-1] < i):
            number_stack.pop()
            k -= 1
        number_stack.append(i)

    if k > 0:
        number_stack = number_stack[:-k]
    
    return ''.join(number_stack)

