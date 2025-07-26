def solution(M, N):
    answer = 0
    
    # 2x2 -> 1x1 => 3
    # 2x5 -> 1x1 => 9
    
    answer = M*N - 1
    
    return answer