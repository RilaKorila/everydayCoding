# C014:ボールが入る箱
# https://paiza.jp/challenges/48/ready

n, r = list(map(int, input().split(" ")))

for box_no in range(1, n + 1):
    h, w, d = list(map(int, input().split(" ")))

    if min(h, w, d) >= 2 * r:
        print(box_no)
