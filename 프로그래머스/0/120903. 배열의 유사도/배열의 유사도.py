def solution(s1, s2):
    answer = 0
    
    if len(s1) >= len(s2):
        for i in range(len(s2)):
            if s2[i] in s1:
                answer += 1
    else:
        for i in range(len(s1)):
            if s1[i] in s2:
                answer += 1
    
    return answer