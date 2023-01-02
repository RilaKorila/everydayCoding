# C013: 嫌いな数字
# https://paiza.jp/challenges/46/ready

hate = int(input())
n = int(input())
ans = []

for i in range(n):
    room = input()
    if hate not in room:
        ans.append(room)

if len(ans) != 0:
    for room in ans:
        print(room)
else:
    print("none")
