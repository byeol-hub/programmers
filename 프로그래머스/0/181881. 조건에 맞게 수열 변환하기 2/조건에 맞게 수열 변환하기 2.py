def solution(arr):
    answer = 0
    a = []
    while (a != arr):
        answer += 1
        a = arr.copy()
        for i in range(len(arr)):
            if arr[i] % 2 == 0 and arr[i] >= 50:
                arr[i] = arr[i] / 2
            elif arr[i] % 2 == 1 and arr[i] < 50:
                arr[i] = arr[i]*2+1
        if a == arr:
            answer -= 1
            break
    return answer