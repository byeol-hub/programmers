def solution(my_string):
    answer = []
    
    for i in range(len(my_string)):
        if my_string[i] < 'a' or my_string[i] > 'z':
            answer.append(int(my_string[i]))
    
    answer.sort()
    
    return answer












# def solution(my_string):
#     answer = []
#     num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
#     for i in my_string:
#         if i in num:
#             answer.append(int(i))
    
#     answer.sort()
    
#     return answer