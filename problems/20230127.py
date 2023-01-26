n = int(input())
a, b = [False for i in range(32)], [False for i in range(32)]

for i in range(n):
    a[int(input())] = True

m = int(input())

for i in range(m):
    b[int(input())] = True

isA_live = True
for day in range(1, 32):
    if a[day] and b[day]:
        print("A" if isA_live else "B")
        isA_live = not isA_live

    elif a[day] or b[day]:
        print("A" if a[day] else "B")

    else:
        print("x")
