def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        answer += 1
        print("case1:",i, answer)
        while (answer % 3 == 0 or "3" in str(answer)):
            if (answer//3 != 0 and answer % 3 == 0):
                answer += 1
                print("case2:",i, answer)
            if answer % 3 != 0 and "3" in str(answer):
                answer += 1
                print("case3:",i, answer)
    
    return answer