# ハイアンドロー・カードゲーム
# https://paiza.jp/challenges/60/ready

parent_a, parent_b = list(map(int, input().split(" ")))
n = int(input())

for i in range(n):
    child_a, child_b = list(map(int, input().split(" ")))
    if parent_a > child_a:
        print("High")
    elif parent_a == child_a and parent_b < child_b:
        print("High")
    else:
        print("Low")
