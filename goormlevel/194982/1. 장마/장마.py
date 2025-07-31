# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N_M = list(map(int, input().split()))
N = list(map(int, input().split()))
M = []
w = [0]*N_M[0]
N_3 = set()
count = 0
result = ''

for i in range(N_M[1]):
	M = list(map(int, input().split()))
	count += 1
	for j in range(M[0]-1,M[1]):
		w[j] += 1
		N_3.add(j)
	if count % 3 == 0:
		for k in range(len(w)):
			if k in N_3:
				w[k] -= 1
		N_3 = set()

for i in range(len(w)):
	N[i] += w[i]

for i in N:
	result += str(i)
	result += ' '

print(result)

