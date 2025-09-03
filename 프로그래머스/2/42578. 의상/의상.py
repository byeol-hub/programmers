def solution(clothes):
    answer = 1
    key_set = []
    
    for i in clothes:
        key_set.append(i[1])

    key_set = list(set(key_set))
    
    clothes_dict = {item: 0 for item in key_set}
    
    for i in clothes:
        for j in key_set:
            if i[1] == j:
                clothes_dict[j] += 1
    
    for i in clothes_dict.keys():
        answer*=clothes_dict[i]+1
    
    return answer-1