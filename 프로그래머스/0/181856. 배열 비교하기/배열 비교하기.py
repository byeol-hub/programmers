def solution(arr1, arr2):
    answer = 0
    arr1_sum = 0
    arr2_sum = 0
    if len(arr1) > len(arr2):
        answer = 1
    elif len(arr1) < len(arr2):
        answer = -1
    else:
        for i in arr1:
            arr1_sum += i
        for i in arr2:
            arr2_sum += i
        if arr1_sum > arr2_sum:
            answer = 1
        elif arr1_sum < arr2_sum:
            answer = -1
    return answer