# 大量出店
# https://paiza.jp/challenges/571/ready

n, m = list(map(int, input().split(" ")))
a, b, c = list(map(int, input().split(" ")))
ans = 0

for i in range(n):
    r = int(input())
    if (c * r < a + b * m):
        ans += 1

print(ans)
