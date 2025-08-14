def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    
    # 9회, 7회, 6회, 2회, 1회의 논문을 5편 발표했다면, 이 저자의 h- 지수는 3입니다. 
    # 왜냐하면 이 저자는 3회 이상 인용된 논문을 3편 보유하고 있기 때문입니다. 
    # 하지만 이 저자는 4회 이상 인용된 논문을 4편 보유하고 있지 않습니다 .
    
    for i in range(len(citations)): 
        if i+1 == citations[i]:
            answer = citations[i]
            break
        
        elif i+1 > citations[i]:
            answer = i
            break
            
        elif i+1 == len(citations):
            answer = i+1
            break
    
    return answer