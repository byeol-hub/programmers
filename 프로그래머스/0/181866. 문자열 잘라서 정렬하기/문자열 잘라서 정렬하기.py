# def solution(myString):
#     answer = []
#     arr = []
#     arr = myString.split('x')
#     for i in range(len(arr)):
#         if arr[i] == "":
#             continue
#         else:
#             answer.append(arr[i])
#     answer.sort()
#     return answer

def solution(myString):
    answer = []
    arr = []
    arr = myString.split('x')
    for i in arr:
        if i == "":
            continue
        else:
            answer.append(i)
    answer.sort()
    return answer