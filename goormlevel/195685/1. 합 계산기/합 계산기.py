# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = int(input())
sum = 0

for i in range(user_input):
	a = input()
	sum += int(eval(a))

print(sum)