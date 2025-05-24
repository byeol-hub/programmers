# def solution(l, r):
#     answer = []
#     for i in range(l,r):
#         if (i % 5 == 0) and (str(i) in "5"):
#             answer.append(i)
#     if answer == []:
#         answer.append(-1)
#     return answer

# def solution(l, r):
#     answer = []
#     for i in range(l,r):
#         if i % 5 == 0:
#             for j in str(i)[:-1]:
#                 if j in "5":
#                     answer.append(i)
#     if answer == []:
#         answer.append(-1)
#     return answer

def solution(l, r):
    answer = []
    for i in range(l,r+1):
        if i % 5 == 0:
            answer.append(i)
            for j in str(i):
                if j in ["1","2","3","4","6","7","8","9"]:
                    answer.remove(i)
                    break
    if answer == []:
        answer.append(-1)
    return answer