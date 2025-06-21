def solution(n):
    answer = [[]]
    answer = [[0 for col in range(n)] for row in range(n)]  
    for i in range(n):
        for j in range(n):
            if j == i:
                answer[i][j] = 1
                break
    return answer