def solution(s):
    answer = []
    
    s_list = list(s)
    
    for i in range(len(s_list)):
        if i == s_list.index(s_list[i]):
            answer.append(-1)
        else:
            answer.append(i-s_list.index(s[i]))
            s_list[s_list.index(s[i])] = s_list[s_list.index(s_list[i])].upper()
    
    return answer