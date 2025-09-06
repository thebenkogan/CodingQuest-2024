from collections import defaultdict
from aoc import nums, read_input


lines = read_input()
costs = defaultdict(int)
for line in lines:
    liner = line.split(": ")[0]
    n = nums(line)[0]
    if "Rebate" in line or "Discount" in line:
        n *= -1
    costs[liner] += n

print(min(costs.values()))
    