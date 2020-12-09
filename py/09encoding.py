with open('inputs/09.txt', 'r') as f:
# with open('test_input.txt', 'r') as f:
    data = [int(i.strip()) for i in f]

preamble = 25

def valid_nbr(nbr, data, preamble_len):
    sum_data = [data[i] + data[j] for i in range(preamble_len) for j in range(preamble_len) if i != j]
    if nbr in sum_data:
        return True
    return False

# Part 1
encoded_nbr = 0
for i in range(len(data)):
    nbr_range = data[i : i+preamble]
    if i + 1 + preamble < len(data): # sanity
        if not valid_nbr(data[i+preamble], nbr_range, preamble):
            encoded_nbr = data[i+preamble]
            print(encoded_nbr)

# Part 2
for i in range(len(data[:-1])):
    sum_range = [data[i], data[i + 1]]
    idx = 2
    while sum(sum_range) < encoded_nbr or i + idx < len(data):
        sum_range.append(data[i + idx])
        idx += 1
        if sum(sum_range) == encoded_nbr:
            print(sum_range)
            min_nbr = min(sum_range)
            max_nbr = max(sum_range)
            print(min_nbr + max_nbr)
            break