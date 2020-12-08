
data = list()
with open('inputs/04.txt', 'r') as f:
    data = [i.strip() for i in f]

fixed_data = list()
tmp_data = list()
for d in data:
    if d == '':
        fixed_data.append(tmp_data)
        tmp_data = list()
    else:
        tmp_data.append(d)

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # , 'cid'] optional

# # Part 1
# valid = 0
# for f_data in fixed_data:
#     print(f_data)
#     data_dic = {}
#     for f_i in f_data:
#         f_i_spaces = f_i.split()
#         for i in f_i_spaces:
#             tmp = i.split(':')
#             data_dic[tmp[0]] = tmp[1]
#     print(data_dic)
#     field_lim = 0
#     for key in data_dic:
#         if key != 'cid':
#             field_lim += 1
#     if field_lim == 7:
#         valid += 1
# print(valid)

# Part 2
def is_valid(field_name, input_data):
    if field_name == 'byr':
        return year_valid(input_data, 1920, 2002)
    elif field_name == 'iyr':
        return year_valid(input_data, 2010, 2020)
    elif field_name == 'eyr':
        return year_valid(input_data, 2020, 2030)
    elif field_name == 'hgt':
        measure = input_data[-2:]
        if measure == 'cm' or measure == 'in':
            height = [i for i in input_data if i.isnumeric()]
            height = int(''.join(height))
            if measure == 'cm':
                return (height >= 150 and height <= 193)
            elif measure == 'in':
                return (height >= 59 and height <= 76)
    elif field_name == 'hcl':
        if input_data[0] != '#':
            return False
        else:
            code = input_data[1:]
            if len(code) != 6:
                return False
            for l in 'ghijklmnopqrstuvwxyz':
                if l in code:
                    return False
        return True
    elif field_name == 'ecl':
        return input_data in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif field_name == 'pid':
        if input_data.isnumeric():
            return len(input_data) == 9
    return False

def year_valid(input_year, nbr_least, nbr_most):
    if int(input_year) >= nbr_least and int(input_year) <= nbr_most:
        return True
    return False

valid = 0
for f_data in fixed_data:
    data_dic = {}
    for f_i in f_data:
        f_i_spaces = f_i.split()
        for i in f_i_spaces:
            tmp = i.split(':')
            data_dic[tmp[0]] = tmp[1]
    field_lim = 0
    print(f_data)
    for key in data_dic:
        print('key: {}, val: {}'.format(key, data_dic[key]))
        if key != 'cid' and is_valid(key, data_dic[key]):
            print('added')
            field_lim += 1
            print(field_lim)
    if field_lim == 7:
        valid += 1
print(valid)

