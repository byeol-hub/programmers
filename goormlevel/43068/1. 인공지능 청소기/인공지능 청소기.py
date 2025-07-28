# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = int(input())
input_arr = []

for i in range(0, user_input):
    input_arr.append(list(map(int, input().split())))
    

for i in range(user_input):
    if (abs(input_arr[i][0]) + abs(input_arr[i][1]) <= input_arr[i][2]) and ((abs(input_arr[i][0]) + abs(input_arr[i][1])) % 2 == input_arr[i][2] % 2):
        print('YES')
        
    else: 
        print('NO')