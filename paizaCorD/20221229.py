# ポイント払い
# https://paiza.jp/works/challenges/359/page/ready

n, m = map(int, input().split(" "))

rest, point = n, 0

for i in range(m):
    fare = int(input())
    if point >= fare:
        point -= fare
    
    else:
        rest -= fare
        point += int(fare * 0.1)

    print(rest, point)
