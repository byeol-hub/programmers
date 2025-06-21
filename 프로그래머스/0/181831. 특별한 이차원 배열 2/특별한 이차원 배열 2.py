def solution(arr):
    answer = 0
    count = 0
    while (count < len(arr)**2):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][j] == arr[j][i]:
                    count += 1
                else:
                    return answer
    if count == len(arr)**2:
        answer = 1
    return answer