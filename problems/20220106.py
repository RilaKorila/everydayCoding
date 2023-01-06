n = int(input())
pre = list(input())
FINISHED = True

for i in range(1, n):
    cur = list(input())
    
    if cur[0] != pre[-1]:
        print(pre[-1], cur[0])
        FINISHED = False
        break
    pre = cur

if FINISHED:
    print('Yes')
