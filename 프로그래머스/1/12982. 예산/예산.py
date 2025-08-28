def solution(d, budget):
    answer = 0
    count = 0
    
    d.sort()
    
    for i in range(len(d)):
        if answer + d[i] <= budget:
            answer += d[i]
            count += 1
        else:
            break
    
    return count