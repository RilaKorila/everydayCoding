# 節分ロボット
# https://paiza.jp/challenges/600/ready

n = int(input())

people = []
ans = [(0,0) for i in range(n)]
for i in range(n):
    people.append((int(input()), 0))

m = int(input())

for command in range(m):
    a, b, c = map(int, list(input().split(' ')))
    
    for j in range(a-1, b):
        year, mame = people[j] 
        mame += c
        if mame >= year:
            people[j] = (year, year)
        else:
            people[j] = (year, mame)

for year, mame in people:
    print(mame)
