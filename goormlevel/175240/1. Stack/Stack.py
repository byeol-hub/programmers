# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = list(map(int, input().split()))

arr = []

for i in range(user_input[0]):
	now = list(input().split())
	if now[0] == 'push':
		if len(arr) < user_input[1]:
			arr.append(int(now[1]))
		else:
			print('Overflow')
	else:
		if arr != []:
			print(arr[-1])
			arr.pop()
		else:
			print('Underflow')