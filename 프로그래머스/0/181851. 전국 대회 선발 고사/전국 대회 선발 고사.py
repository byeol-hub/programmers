def solution(rank, attendance):
    answer = 0
    temp = 0
    arr = []
    b = []
    c = []
    sort_rank = sorted(rank)
    for i in range(len(rank)):
        b.append(i)
    print(b)
    while (rank != sort_rank):
        for i in range(len(rank)-1):
            if rank[i] > rank[i+1]:
                temp = rank[i]
                rank[i] = rank[i+1]
                rank[i+1] = temp
                temp = attendance[i]
                attendance[i] = attendance[i+1]
                attendance[i+1] = temp
                temp = b[i]
                b[i] = b[i+1]
                b[i+1] = temp
    print(rank)
    print(attendance)
    print(b)
    for i in range(len(rank)):
        if attendance[i] == True:
            arr.append(rank[i])
            c.append(b[i])
    print(arr)
    print(c)
    answer = 10000*c[0] + 100*c[1] + c[2]
    return answer