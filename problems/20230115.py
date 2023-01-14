# RPGでお買い物
# https://paiza.jp/challenges/424/ready

from curses.ascii import isdigit

n = int(input())
price = list(map(int, input().split()))
money, order_num = list(map(int, input().split()))

for i in range(order_num):
    item, n = list(map(int, input().split()))
    if n * price[item - 1] <= money:
        money -= n * price[item - 1]

print(money)

# クジの当選番号
# https://paiza.jp/challenges/85/ready

bingo = set(map(int, input().split()))
n = int(input())

for i in range(n):
    kuji = list(map(int, input().split()))
    print(sum(list(map(lambda x: 1 if x in bingo else 0, kuji))))

# 黒電話
# https://paiza.jp/challenges/433/ready
s = input()
ans = 0
d = {0: 12, 1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8, 7: 9, 8: 10, 9: 11}

for c in s:
    if c.isdigit():
        ans += d[int(c)] * 2

print(ans)
