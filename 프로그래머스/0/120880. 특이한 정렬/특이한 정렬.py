def solution(numlist, n):
    answer = []
    numlist_dis = []
    numlist_dis_sort = []
    
    numlist.sort(reverse = True)
    
    for i in numlist:
        numlist_dis.append(abs(n-i))
    
    for i in range(len(numlist_dis)):
        answer.append(numlist[numlist_dis.index(min(numlist_dis))])
        numlist_dis[numlist_dis.index(min(numlist_dis))] += 10001      
    
    return answer