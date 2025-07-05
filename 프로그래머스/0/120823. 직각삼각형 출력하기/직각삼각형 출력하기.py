n = int(input())

for i in range(1, n+1):
    n_print = ''
    for j in range(i):
        n_print += '*'
    print(n_print)
