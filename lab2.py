L = []

L = [[1, 1], [0, 1]]
print('Sanath 1BM23CS297')
print(L)
count = 0
for i in range(len(L)):
    if (L[i][1] == 1):
        count = count + 1

def clean(L, count, index):
    if (count == 0):
        return

    if (index < 0 or index >= len(L)):
        return

    if (L[index][1] == 1):
        
        L[index][0] = 1
        L[index][1] = 0
        count = count - 1
        print(L)
        L[index][0] = 0
        
        clean(L, count, index - 1)
        clean(L, count, index + 1)
    else:
        clean(L, count, index + 1)
        clean(L, count, index - 1)

    

clean(L, count, 0)