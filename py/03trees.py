data = list()
with open('inputs/11.txt', 'r') as f:
    data = [i.split('\n')[0] for i in f]

# right_slope = 3
# down_slope = 1

# slope = list()
# tree = 0
# while down_slope < len(data):
#     print(data[down_slope])
#     # print(len(data[down_slope]))
#     r = (right_slope) % len(data[down_slope])
#     print(r)
#     track = data[down_slope][r]
#     down_slope += 1
#     right_slope += 3
#     slope.append(track)
#     if track == '#':
#         tree += 1
# print(slope)
# print(tree)

right_slope = [1, 3, 5, 7, 1]
down_slope = [1, 1, 1, 1, 2]

mul_tree = list()
for i in range(len(right_slope)):
    tree = 0
    right = right_slope[i]
    down = down_slope[i]
    while down < len(data):
        r = (right) % len(data[down])
        track = data[down][r]
        down += down_slope[i]
        right += right_slope[i]
        if track == '#':
            tree += 1
    mul_tree.append(tree)
print(mul_tree)
score = 1
for ml in mul_tree:
    score *= ml
print(score)