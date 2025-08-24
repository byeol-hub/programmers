def solution(s):
    answer = True
    count_0 = 0
    
    if s[0] == ")" or s[len(s)-1] == "(":
        return False
    
    for i in range(len(s)):
        if count_0 < 0:
            return False
        if s[i] == "(":
            count_0 += 1
        else:
            count_0 -= 1
    
    if count_0 != 0:
        return False

    return True