a, b = map(int, input().strip().split(' '))

for i in range(b):
    result = ''
    for j in range(a):
        result += '*'
    print(result)