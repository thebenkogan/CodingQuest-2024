from aoc import nums, read_input

line = read_input(split_lines=False)
ns = nums(line)

W = 100
H = 80

screen = [["."] * W for _ in range(H)]
is_dot = False
x, y = 0, 0
for n in ns:
    is_dot = not is_dot
    if is_dot:
        y += (x + n) // W
        x = (x + n) % W
        continue

    for _ in range(n):
        screen[y][x] = "#"
        x += 1
        if x >= W:
            x = 0
            y += 1

for row in screen:
    print("".join(row))
