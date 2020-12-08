with open('inputs/06.txt', 'r') as f:
# with open('test_input.txt', 'r') as f:
    data = [i.strip() for i in f]
data.append('')

# Part 1
group_counts = list()
nbr_yes = dict()
for d in data:
    if d == '':
        group_counts.append(len(nbr_yes))
        nbr_yes = dict()
    else:
        for l in d:
            nbr_yes[l] = 1
    
print(sum(group_counts))

# Part 2
groups = list()
tmp_group = list()
group_counts = list()
for d in data:
    if d == '':
        groups.append(tmp_group)
        tmp_group = list()
    else:
        tmp_group.append(d)
    
for g in groups:
    group_dict = dict()
    for g_i in g:
        for i in g_i:
            if i in group_dict:
                group_dict[i] += 1
            else:
                group_dict[i] = 1
    cnt = 0
    for key in group_dict:
        if group_dict[key] == len(g):
            cnt += 1
    group_counts.append(cnt)
print(sum(group_counts))