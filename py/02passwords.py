data_input = list()
with open('inputs/02.txt', 'r') as input_file:
    for i in input_file:
        data_input.append(i.split('\n')[0])

print(data_input)

# # Part 1
# valid = 0
# for d in data_input:
#     data = d.split()
#     lower, upper = map(int, data[0].split('-'))
#     policy_char = data[1].split(':')[0]
#     print('Data: {}, lower: {}, upper: {}, policy_char: {}'.format(d, lower, upper, policy_char))
#     filtered = list(filter(lambda x: x is policy_char, data[2]))
#     if len(filtered) >= lower and len(filtered) <= upper:
#         valid += 1
# print(valid)

# Part 2
valid = 0
for d in data_input:
    data = d.split()
    policy_idx1, policy_idx2 = map(int, data[0].split('-'))
    policy_char = data[1].split(':')[0]
    # filtered = list(filter(lambda x: x is policy_char, data[2]))
    password = data[2]
    print('Password: {}, char: {}, idx1: {}, idx2: {}'.format(password, policy_char, policy_idx1, policy_idx2))
    if bool(password[policy_idx1 - 1] == policy_char) ^ bool(password[policy_idx2 - 1] == policy_char):
        # print('hit')
        valid += 1
print(valid)
