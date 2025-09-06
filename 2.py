from aoc import  read_input

internal_min = [192,168,0,0]
internal_max = [192,168,254,254]

passenger_min = [10,0,0,0]
passenger_max = [10,0,254,254]

def in_range(min, max, ip):
    for (l,h), n in zip(zip(min,max), ip):
        if n < l or n > h:
            return False
    return True

lines = read_input()
internal_total = 0
passenger_total = 0
for line in lines:
    bs = bytes.fromhex(line)
    length = int.from_bytes(bs[2:4], "big")
    source = [int(b) for b in bs[12:16]]
    dest = [int(b) for b in bs[16:20]]
    if any(in_range(internal_min, internal_max, ip) for ip in [source, dest]):
        internal_total += length
    if any(in_range(passenger_min, passenger_max, ip) for ip in [source, dest]):
        passenger_total += length

print(f"{internal_total}/{passenger_total}")

