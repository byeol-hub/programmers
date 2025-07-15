def solution(score):
    answer = []
    score_mean = []
    score_sort = []
    
    for i,j in score:
        score_mean.append((i+j)/2)
    
    score_sort = sorted(score_mean, reverse=True)
    
    for i in range(len(score_mean)):
        for j in range(len(score_sort)):
            if score_sort[j] == score_mean[i]:
                answer.append(j+1)
                break
    
    return answer