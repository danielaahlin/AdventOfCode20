with open('inputs/08.txt', 'r') as f:
# with open('test_input.txt', 'r') as f:
    data = [i.strip() for i in f]

def loop(data, bool_data, idx, acc):
    while not bool_data[idx]:
        operation, value = data[idx].split()

        bool_data[idx] = True
        if operation == 'nop':
            idx += 1
        elif operation == 'acc':
            acc += int(value)
            idx += 1
        else: # operation == 'jmp':
            idx += int(value)
        
        # Part 2
        if idx >= len(data):
            print(acc)
            return True

    # print(acc) # Part 1
    return False # Part 2

# Part 1
loop(data, [False for _ in range(len(data))], 0, 0)

# Part 2
for i in range(len(data)):
    d = data[i]
    if 'nop' in d:
        tmp_d = 'jmp {}'.format(d.split()[1])
        data[i] = tmp_d
        if loop(data, [False for _ in range(len(data))], 0, 0):
            break
        else:
            data[i] = d
    elif 'jmp' in d:
        tmp_d = 'nop {}'.format(d.split()[1])
        data[i] = tmp_d
        if loop(data, [False for _ in range(len(data))], 0, 0):
            break
        else:
            data[i] = d