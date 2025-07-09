def solution(num_list, n):
    answer = [[]]
    num = 0
    
    for i in range(0, len(num_list), n):
        print(i, n*(i+1))
        num += 1
        answer.append(num_list[i:n*num])
    
    if [] in answer:
        answer.remove([])
    
    return answer