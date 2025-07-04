def solution(array):
    answer = 0
    answer_arr = []
    
    array_set = set(array)
    array_set = list(array_set)
    print(array_set)
    
    arr = []
    
    arr_max = 0
    
    for i in range(len(array_set)):
        arr.append(0)
    
    for i in array:
        for j in range(len(array_set)):
            if i == array_set[j]:
                arr[j] += 1
                break
    
    print(arr)
    
    arr_max = max(arr)
    
    print(arr_max)
    
    for i in range(len(arr)):
        if arr[i] == arr_max:
            answer_arr.append(i)
    
    print(answer_arr)
    
    if len(answer_arr) != 1:
        answer = -1
    else:
        answer = array_set[answer_arr[0]]
     
    return answer