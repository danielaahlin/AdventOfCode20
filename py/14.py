with open('test_input.txt', 'r') as f:
# with open('inputs/14.txt', 'r') as f:
    data = [i.strip() for i in f]
print(data)

mem = dict()
mask = data[0].split('=')[1]
print(mask)

for instruction in data:
    if 'mem' in instruction:
        split_instr = instruction.split()
        mem_idx = split_instr[0][4:-1]
        mem_value = split_instr[2]
        print(mem_idx)
        print(mem_value)
    else:
        mask = instruction.split('=')[1]