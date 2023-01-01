# C052:ゲームの画面
# https://paiza.jp/works/challenges/246/ready

h, w = list(map(int, input().split(" ")))
dy, dx = list(map(lambda n: abs(int(n)), input().split(" ")))

print((w * dy + h * dx - dy * dx))
