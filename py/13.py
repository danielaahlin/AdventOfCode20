# with open('test_input.txt', 'r') as f:
with open('inputs/13.txt', 'r') as f:
    data = [i.strip() for i in f]
# print(data)

my_timestamp = int(data[0])
bus_ids = [int(x) for x in data[1].split(',') if x != 'x']
# print(my_timestamp)
# print(bus_ids)

timestamps = dict()
for ids in bus_ids:
    close_stamp = my_timestamp // ids
    timestamps[ids] = (close_stamp, close_stamp + 1)
# print(timestamps)

all_timestamps = []
for t in timestamps:
    all_timestamps.append(t * timestamps[t][0] if t * timestamps[t][0] >= my_timestamp else 0)
    all_timestamps.append(t * timestamps[t][1] if t * timestamps[t][1] >= my_timestamp else 0)
# print(all_timestamps)

timestamp_idx = list(map(lambda x : abs(x - my_timestamp), all_timestamps))
# print(timestamp_idx)
wait_time = min(timestamp_idx)
idx = timestamp_idx.index(wait_time)

bus = bus_ids[idx // 2]
print(bus)

print(bus * wait_time)