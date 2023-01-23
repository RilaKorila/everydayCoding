k, n = list(map(int, list(input().split())))

haiten = 100 / n

for i in range(k):
    d, a = list(map(int, list(input().split())))

    score = a * haiten
    if d >= 10:
        score = 0
    elif d > 0:
        score = score * 0.8

    if score >= 80:
        print("A")
    elif score >= 70:
        print("B")
    elif score >= 60:
        print("C")
    else:
        print("D")
