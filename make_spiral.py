"""Your task, is to create a NxN spiral with a given size.

For example, spiral with size 5 should look like this:

00000
....0
000.0
0...0
00000
and with the size 10:

0000000000
.........0
00000000.0
0......0.0
0.0000.0.0
0.0..0.0.0
0.0....0.0
0.000000.0
0........0
0000000000
Return value should contain array of arrays, of 0 and 1, with the first row being composed of 1s. For example for given size 5 result should be:

[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Because of the edge-cases for tiny spirals, the size will be at least 5.

General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself."""


def can_move_to(nr, nc, size, grid):
    if not (0 <= nr < size and 0 <= nc < size):
        return False
    if grid[nr][nc] == 1:
        return False
    neighbors = [(nr - 1, nc), (nr + 1, nc), (nr, nc - 1), (nr, nc + 1)]
    ones = 0
    for rr, cc in neighbors:
        if 0 <= rr < size and 0 <= cc < size and grid[rr][cc] == 1:
            ones += 1
    return ones <= 1


def spiralize(size):
    grid = [[0] * size for _ in range(size)]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_index = 0
    r = c = 0
    grid[r][c] = 1

    while True:
        moved = False
        for attempt in range(4):
            dr, dc = dirs[dir_index]
            nr, nc = r + dr, c + dc
            if can_move_to(nr, nc, size, grid):
                r, c = nr, nc
                grid[r][c] = 1
                moved = True
                break
            dir_index = (dir_index + 1) % 4

        if not moved:
            break

    return grid
