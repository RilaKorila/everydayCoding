b, a = input().split()

b_score, a_score = (
    str(sum(list(map(int, list(b)))))[-1],
    str(sum(list(map(int, list(a)))))[-1],
)

if b_score < a_score:
    print("Alice")
elif b_score > a_score:
    print("Bob")
else:
    print("Draw")
