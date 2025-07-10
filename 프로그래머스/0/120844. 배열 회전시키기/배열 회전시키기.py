def solution(numbers, direction):
    answer = []
    
    # right -> 맨 마지막 원소가 맨 처음으로 가고 나머지 원소들의 인덱스는 +1씩 이동
    # left -> 맨 처음 원소가 맨 마지막으로 가고 나머지 원소들의 인덱스는 -1씩 이동
    
    if direction == "right":
        answer.append(numbers[-1])
        for i in numbers[:-1]:
            answer.append(i)
    else:
        for i in numbers[1:]:
            answer.append(i)
        answer.append(numbers[0])
    
    return answer