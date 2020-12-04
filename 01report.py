with open('01input.txt', 'r') as f:
    nbrs = [int(i) for i in f]
print(nbrs)

# # Part 1
# for i in nbrs:
#     for j in nbrs:
#         if i != j and i + j == 2020:
#             tup = (i, j)
# print(tup)
# print('Answer: {}'.format(tup[0] * tup[1]))

# Part 2
for i in nbrs:
    for j in nbrs:
        for k in nbrs:
            if i != j != k and i + j + k == 2020:
                tup = (i, j, k)
                
tp = [i * j * k for i in nbrs for j in nbrs for k in nbrs if i != j != k and i + j + k == 2020]
print(tp)
print(tup)
print('Answer: {}'.format(tup[0] * tup[1] * tup[2]))