# Find value of X such that it has exactly K bits and Sum(A[i]&X) is maximum.
# If there are multiple values for X return lowest

# def bin_to_dec(bin_x):
#     bin_x = str(bin_x)
#     dec = 0
#     for i in range(len(bin_x)):
#         ele = int(bin_x[i])
#         if ele == 1:
#             dec += 2 ** i
#     return dec


N = int(input())
A = []

for i in range(N):
    A.append(int(input()))

K = int(input())
OR_op = A[0]
for ele in A[1:]:
    OR_op |= ele
OR_op = str(bin(OR_op))[2:]

bin_x = 0
cnt = 0
for i in range(len(OR_op)):
    if OR_op[i] == '1' and cnt < K:
        bin_x = bin_x * 10 + 1
        cnt += 1
    else:
        bin_x *= 10

if cnt < K:
    r = 0
    for i in range((K - cnt)):
        r = r * 10 + 1
    bin_x += r

bin_x = str(bin_x)[::-1]

x = 0
for i in range(len(bin_x)):
    ele = int(bin_x[i])
    if ele == 1:
        x += 2 ** i

print(x)
