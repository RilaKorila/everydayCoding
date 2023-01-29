attack, defence, agility = list(map(int, input().split()))
n = int(input())

EVOLUTION = False
for i in range(n):
    info = input().split()
    name = info[0]
    MINATK, MAXATK, MINDEF, MAXDEF, MINAGI, MAXAGI = list(map(int, info[1:]))

    if (
        (MINATK <= attack <= MAXATK)
        and (MINDEF <= defence <= MAXDEF)
        and (MINAGI <= agility <= MAXAGI)
    ):
        EVOLUTION = True
        print(name)

if not EVOLUTION:
    print("no evolution")
