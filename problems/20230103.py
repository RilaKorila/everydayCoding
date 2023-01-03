# C055:ログのフィルター
# https://paiza.jp/works/challenges/261/ready

n = int(input())
target = input()
ans = []

for i in range(n):
    s = input()
    if target in s:
        ans.append(s)

if len(ans) != 0:
    for log in ans:
        print(log)
else:
    print("None")
