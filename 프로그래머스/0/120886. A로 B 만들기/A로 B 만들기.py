def solution(before, after):
    answer = 1
    before_unique = list(set(before))
    after_unique = list(set(after))
    
    # before와 after의 요소와 개수가 모두 같아야 함
    
    if set(before) != set(after):
        answer = 0
        return answer
    else:
        for i in range(len(before_unique)):
            if before.count(before_unique[i]) != after.count(before_unique[i]):
                answer = 0
                return answer
    
    return answer