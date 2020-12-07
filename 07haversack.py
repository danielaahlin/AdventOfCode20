with open('inputs/07.txt', 'r') as f:
# with open('test_input.txt', 'r') as f:
    data = [i.strip() for i in f]

sorted_data = dict()
for d in data:
    split = d.split()
    key = split[0] + ' ' + split[1]
    if split[4] == 'no':
        value = 'no other bags'
        sorted_data[key] = [value]
    else:
        val_split = split[4:]
        vals = list()
        while len(val_split) > 0:
            value = val_split[0] + ' ' + val_split[1] + ' ' + val_split[2]
            val_split = val_split[4:]

            vals.append(value)
        sorted_data[key] = vals

def number_bags(bag_color):
    if 'no other bags' in bag_color[0]:
        return 0
    elif 'shiny gold' in ''.join(bag_color):
        return 1
    
    for bag in bag_color:
        if number_bags(sorted_data[bag[2:]]) == 1:
            return 1
    return 0

def nbrs_bags_total(bag_color):
    nbr_sum = 0
    if 'no other bags' in bag_color[0]:
        return 0
    for bag in bag_color:
        nbr = int(bag[0])
        nbr_sum += nbr + nbr * nbrs_bags_total(sorted_data[bag[2:]])
    return nbr_sum

nbrs = list()
for s in sorted_data:
    nbrs.append(number_bags(sorted_data[s])) # Part 1
print(sum(nbrs))

# Part 2 
print(nbrs_bags_total(sorted_data['shiny gold']))
