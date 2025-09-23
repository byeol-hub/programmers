def solution(park, routes):
    answer = []
    
    # 시작 위치 찾기
    for i in range(len(park)):
        if 'S' in park[i]:
            answer.append(i)
            answer.append(park[i].index('S'))
            break
    
    # 산책 진행
    for i in routes:
        if i[0] == "E":  # 오른쪽
            if answer[1] + int(i[2:]) < len(park[0]):
                for j in range(1, int(i[2:])+1):
                    if park[answer[0]][answer[1] + j] == 'X':
                        break
                else:
                    answer[1] += int(i[2:])
        elif i[0] == "S":  # 아래
            if answer[0] + int(i[2:]) < len(park):
                for j in range(1, int(i[2:])+1):
                    if park[answer[0] + j][answer[1]] == 'X':
                        break
                else:
                    answer[0] += int(i[2:])
        elif i[0] == "W":  # 왼쪽
            if answer[1] - int(i[2:]) >= 0:
                for j in range(1, int(i[2:])+1):
                    if park[answer[0]][answer[1] - j] == 'X':
                        break
                else:
                    answer[1] -= int(i[2:])
        else:  # 위
            if answer[0] - int(i[2:]) >= 0:
                for j in range(1, int(i[2:])+1):
                    if park[answer[0] - j][answer[1]] == 'X':
                        break
                else:
                    answer[0] -= int(i[2:])
    
    return answer
