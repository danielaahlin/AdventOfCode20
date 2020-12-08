with open('inputs/05.txt', 'r') as f:
    data = [i.strip() for i in f]
print(data)

# max_val are equal to the binary number of places
# for rows = 128, for cols = 8
def get_place(max_val, letters):
    binary_steps = list()
    l_range = [0, max_val-1]
    while max_val != 1:
        max_val = int(max_val/2)
        binary_steps.append(max_val)
    for i in range(len(letters)):
        if letters[i] == 'F' or letters[i] == 'L':
            l_range[1] -= binary_steps[i]
        elif letters[i] == 'B' or letters[i] == 'R':
            l_range[0] += binary_steps[i]
    return l_range[0]

seat_ids = list()

for d in data:
    row_letters = d[:7]
    col_letters = d[7:]

    row = get_place(128, row_letters)
    col = get_place(8, col_letters)
    seat_id = row * 8 + col

    seat_ids.append(seat_id)
    # print('Row: {}, Col: {}, SeatID: {}'.format(row, col, seat_id))
print(max(seat_ids))

seat_ids.sort()
for s in range(len(seat_ids)):
    if seat_ids[s + 1] - seat_ids[s] != 1:
        print(seat_ids[s + 1] - 1)
        break