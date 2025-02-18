import os

def minimum_moves(grid, startX, startY, goalX, goalY):
    rows = len(grid)
    columns = len(grid[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited_states = set()
    visited_states.add((startX, startY))
    queue = [(startX, startY, 0)]
    while queue:
        sx, sy, moves = queue.pop(0)
        if (sx, sy) == (goalX, goalY):
            return moves
        for x, y in directions:
            nx, ny = sx, sy
            while 0 <= nx + x < rows and 0 <= ny + y < columns and grid[nx + x][ny + y] != 'X':
                nx += x
                ny += y
                if (nx, ny) not in visited_states:
                    visited_states.add((nx, ny))
                    queue.append((nx, ny, moves + 1))
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()
    startX = int(first_multiple_input[0])
    startY = int(first_multiple_input[1])
    goalX = int(first_multiple_input[2])
    goalY = int(first_multiple_input[3])
    result = minimum_moves(grid, startX, startY, goalX, goalY)
    fptr.write(str(result) + '\n')
    fptr.close()
