
for c in range(0, 10):
    print('* ', end='')
    for a in range(0, 10):
        if c == 9 or c == 0:
            print('*', end=' ')
        else:
            print('1', end=' ')
    print('*')
