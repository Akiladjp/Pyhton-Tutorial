for i in range(5):
    for j in range(i+1):
        print('x', end='')
    print()
for i in range(5):
    for j in range(4-i):
        print('x', end='')
    print()



n = 5;

for i in range(n):
    for k in range(n-i):
        print(' ', end='')
    for j in range(i+1):
        print('x', end='')
    print()
    

