n, m = list(map(int, list(input().split())))
instruction = ["" for i in range(n)]

for i in range(m):
    time, inst = input().split()

    j = 1
    while j * int(time) <= n:
        instruction[j * int(time) - 1] += inst + " "
        j += 1

for i, inst in enumerate(instruction):
    if inst == "":
        print(i + 1)
    else:
        print(inst[:-1])


# instruction = {}
# for i in range(m):
#     # get inputs
#     time, inst = input().split()

#     if instruction.get(int(time)) is not None:
#         instruction[int(time)].append(inst)
#     else:
#         instruction[int(time)] = [inst]

# for i in range(1, n+1):
#     ans = ""

#     for j in range(1, i + 1):
#         if i % j == 0:
#         #   inst = instruction.get(j, "")
#             if instruction.get(j) is not None:
#                 print("j: ", str(j), " inst: ", instruction[j])
#                 ans += " ".join(instruction[j])
#                 ans += " "
#     if ans == "":
#         print(i)
#     else:
#         print(ans[:-1])
# print(instruction)
