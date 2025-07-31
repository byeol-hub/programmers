# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = list(map(int, input().split()))
result = str(f"{((user_input[0]*7) / (user_input[0] + user_input[1])):.3f}")[:-1]
print(result)