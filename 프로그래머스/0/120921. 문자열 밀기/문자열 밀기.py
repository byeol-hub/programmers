def solution(A, B):
    answer = 0
    arr_A = ''
    
    if A == B:
        return answer
        
    for i in range(len(A)):
        if arr_A == B:
            break
        else:
            arr_A = A[-1:-i-2:-1][::-1] + A[:-i-1]
            answer += 1
        
    if answer == len(A):
        answer = -1
    
    return answer