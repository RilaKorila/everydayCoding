# IDを登録順に並べよう
# https://paiza.jp/works/challenges/535/ready

n = int(input())
d = {}

for i in range(n):
    s = list(input())
    for j, c in enumerate(s):
        if c.isdigit():
            name = "".join(s)
            num = int("".join(s[j:]))
            break
    d[num] = name

keys = sorted(list(d.keys()))

for name in list(map(lambda k: d[k], keys)):
    print(name)
