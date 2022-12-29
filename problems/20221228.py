# Leet文字列
# https://paiza.jp/challenges/54/ready

s = list(input())

leet = {"A": "4", "E": "3", "G": "6", "I": "1", "O": "0", "S": "5", "Z": "2"}

for i, c in enumerate(s):
    if c in leet.keys():
        s[i] = leet[c]

print("".join(s))
