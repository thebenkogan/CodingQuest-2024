import re
from aoc import nums, read_input

data = read_input(split_lines=False)
matrix, routes = data.split("\n\n")
matrixLines = matrix.split("\n")
routesLines = routes.split("\n")

nodes = {n: i for (i, n) in enumerate(re.findall(r"\w+", matrixLines[0]))}
matrix = []
for line in matrixLines[1:]:
    split = line.split(" ")
    rest = " ".join(split[1:])
    matrix.append(nums(rest))

total = 0
for route in routesLines:
    path = route.split(": ")[1].split(" -> ")
    for i in range(len(path) - 1):
        source = nodes[path[i]]
        dest = nodes[path[i + 1]]
        total += matrix[source][dest]

print(total)
