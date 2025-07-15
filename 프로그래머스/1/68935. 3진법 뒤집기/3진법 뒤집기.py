def solution(n):
    answer = 0
    n_3 = ''
    
    # 3진법: 0, 1, 2만 사용
    
    while n != 0:
        n_3 += str(n%3)
        n = n//3
    
    for i in range(len(n_3)):
        answer += int(n_3[-i-1])*(3**int(i))
    
    return answer