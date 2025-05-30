def solution(my_string, is_suffix):
    answer = 0
    arr = []
    for i in range(len(my_string)):
        arr.append(my_string[i:])
    for i in arr:
        if i == is_suffix:
            answer = 1
            break
    return answer