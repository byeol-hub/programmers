def solution(box, n):
    answer = 1
    
    # 놓을 수 있는 블럭 수 = 각 원소 // n
    # 가로에 놓을 수 있는 블럭 수 * 세로에 놓을 수 있는 블럭 수 * 높이에 놓을 수 있는 블럭 수
    
    for i in box:
        answer *= i // n
    
    return answer