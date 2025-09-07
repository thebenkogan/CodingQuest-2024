from dataclasses import dataclass
import math
import re
from aoc import read_input


@dataclass
class Star:
    name: str
    x: float
    y: float
    z: float

    def dist(self, other):
        return math.sqrt(
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        )


lines = read_input()
stars = []
for line in lines[1:]:
    split = line.split("  ")
    name = split[0]
    rest = " ".join(split[1:])
    x, y, z = [float(n) for n in re.findall(r"(-?\d+\.\d+)", rest)][1:]
    stars.append(Star(name, x, y, z))

best = 1e10
for i in range(len(stars)):
    for j in range(i + 1, len(stars)):
        best = min(best, stars[i].dist(stars[j]))

print(round(best, 3))
