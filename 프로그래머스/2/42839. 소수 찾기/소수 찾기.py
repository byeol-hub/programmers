def solution(numbers):
    answer = 0
    numbers_list = set()
    
    # numbers의 범위가 매우 작기 때문에 여러번 반복을 거치는 것이 가능함
    from itertools import permutations
    
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            if "".join(j)[0] != '0':
                numbers_list.add(int("".join(j)))
    
    for i in numbers_list:
        if i == 2:
            answer += 1
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i-1:
                answer += 1
    
    # 1,2,6,9,10
    
    return answer