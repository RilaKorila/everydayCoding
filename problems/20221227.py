# ハンドルネームの生成
# https://paiza.jp/challenges/416/ready

s = list(input())
vowel = ("a", "i", "u", "e", "o", "A", "I", "U", "E", "O")
ans_ind = []

for i, c in enumerate(s):
    if c not in vowel:
        ans_ind.append(i)

print("".join(map(lambda i: s[i], ans_ind)))
