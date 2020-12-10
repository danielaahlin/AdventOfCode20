with open('test_input.txt', 'r') as f:
# with open('inputs/10.txt', 'r') as f:
    data = [int(i.strip()) for i in f]
data.sort()

# Part 1
diffs = {1: [], 2: [], 3: []}
joltage = 0

all_diffs = []

for d in data:
    diff = d - joltage
    if diff < 4:
        diffs[diff].append(d)
        joltage = d
diffs[3].append(joltage + 3)
all_diffs.append(diffs)

print(all_diffs)
print(len(all_diffs[0][1]) * len(all_diffs[0][3]))

# Part 2
print(data)
paths = 0
def find_paths(start, finish, visited, graph, path):
    global paths
    visited[data.index(start)] = True
    path.append(start)

    if start == finish:
        paths += 1
        # print(path)
    else:
        for i in graph[start]:
            # print(i)
            if visited[data.index(i)] == False:
                find_paths(i, finish, visited, graph, path)
    path.pop()
    visited[data.index(start)] = False

graph = dict()
for i in range(len(data)):
    edge = data[i]
    graph[edge] = list()
    # print(edge)
    idx = 1
    while i + idx < len(data) and data[i + idx] - edge < 4:
        graph[edge].append(data[i + idx])
        idx += 1

print(graph)
start_points = [d for d in data if d < 4]
print(start_points)
for s_p in start_points:
    print(s_p)
    find_paths(min(data), max(data), [False for _ in range(len(data))], graph, [])
    print(paths)
print(paths)