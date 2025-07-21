def solution(my_string):
    answer = 0
    arr = ''
    
    if my_string.isalpha():
        return answer
    
    my_string = my_string.lower()
    my_string += 'a'
    
    for i in range(len(my_string)-1):
        if ('a'<=my_string[i]<='z'):
            if my_string[i+1].isdigit():
                arr += '+'
            else:
                continue
        else:
            arr += my_string[i]
            
    answer = eval(arr)
    
    return answer

# def solution(my_string):
#     answer = 0
#     arr = ''
#     num = ''
#     number = ['0','1','2','3','4','5','6','7','8','9']
    
#     my_string = my_string.lower()
#     my_string += 'a'
    
#     for i in range(len(my_string)-1):
#         if ('a'<=my_string[i]<='z') and (my_string[i+1] in number):
#             arr += '+'
#         elif 'a'<=my_string[i]<='z':
#             continue
#         else:
#             arr += my_string[i]
            
#     answer = eval(arr)
    
#     return answer

# def solution(my_string):
#     answer = 0
#     arr = []
#     num = ''
    
#     my_string = my_string.lower()
    
#     for i in my_string:
#         if 'a'<=i<='z':
#             arr.append('')
#         else:
#             arr.append(i)
    
#     for i in range(len(arr)):
#         if arr[i] == '':
#             continue
#         elif arr[i+1] != '':
#             num += arr[i]
#         elif num != '':
#             num += arr[i]
#             answer += int(num)
#             num = ''
#         else:
#             answer += int(arr[i])
    
#     return answer