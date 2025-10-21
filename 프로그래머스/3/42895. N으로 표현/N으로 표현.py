def solution(N, number):
    
    dp = [set() for _ in range(8)]
    
    for i in range(1,9):
        dp[i-1].add(int(str(N)*i))
    
    for i in range(8):
        for j in range(i):
            for a in dp[j]:
                for b in dp[i-j-1]:
                    dp[i].add(a+b)
                    dp[i].add(a-b)
                    dp[i].add(a*b)
                    if b != 0:
                        dp[i].add(a//b) # 나누기 연산에서 나머지는 무시함
        if number in dp[i]:
            return i + 1
    
    return -1
