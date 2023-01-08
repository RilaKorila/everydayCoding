n = int(input())
balls = [int(input()) for i in range(n)]

m = int(input())


for i in range(m):
    pass_from, pass_to, passed_ball = list(map(int, input().split(" ")))
    if balls[pass_from - 1] <= passed_ball:
        passed_ball = balls[pass_from - 1]

    balls[pass_from - 1] -= passed_ball
    balls[pass_to - 1] += passed_ball

for ball in balls:
    print(ball)
