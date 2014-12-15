seq = [5, 3, 7, 8, 2, 4, 1, 6, 1]

# max_length = 0
# l = [1] * seq.__len__()
# n = 0
# for i in range(1, seq.__len__()):
#     for j in range(i):
#         if seq[n] <= seq[j]:
#             l[i] += l[n]
#             n = i
# print l
max_len = 1
for i in range(len(seq)):
    l = 0
    last = seq[i]
    for j in range(i, len(seq)):
        if last <= seq[j]:
            l += 1
            last = seq[j]

    max_len = max(l, max_len)

print max_len