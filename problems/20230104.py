# C115:渋滞の距離
# https://paiza.jp/challenges/560/ready

n, m = list(map(int, input().split(" ")))
ans = 0

for i in range(n - 1):
    distance = int(input())
    if distance <= m:
        ans += distance

print(ans)
