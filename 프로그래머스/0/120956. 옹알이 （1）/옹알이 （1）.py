def solution(babbling):
    answer = 0
    arr = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        a = 0
        while a < len(i):
            arr_in = 0
            for j in arr:
                if i[a:a+len(j)] == j:
                    a += len(j)
                    arr_in = 1
                    break
            if arr_in == 0:
                break
        else:
            answer += 1
                
    return answer