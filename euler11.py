# Program to parse a nxn grid and
# find the greatest product of
# four consecutive integers
from threading import Thread

# Read the grid from a text file,
# and store it as a variable
largest = 0
def gridCreate():
    grid = []
    gridFile = open('grid.txt');
    for lines in gridFile.readlines():
        gridLine = lines.strip('\n')
        grid.append(map(int, lines.split(' ')))
    return grid

# Check each value of the grid and the
# next three values
def findLargest(grid, x, y):
    cur = grid[x][y]
    global largest;

    # right
    for i in range(1, 4):
        if y+i < len(grid):
            cur = cur*grid[x][y+i]
    if cur > largest:
        largest = cur

    cur = grid[x][y]
    # left
    for i in range(1, 4):
        if y-i >= 0:
            cur = cur*grid[x][y-i]
    if cur > largest:
        largest = cur

    cur = grid[x][y]
    # top
    for i in range(1, 4):
        if x+i < len(grid):
            cur = cur* grid[x+i][y]
    if cur > largest:
        largest = cur

    cur = grid[x][y]
    # bottom
    for i in range(1, 4):
        if x-i >= 0:
            cur = cur * grid[x-i][y]
    if cur > largest:
        largest = cur

    cur = grid[x][y]
    # top-left
    for i in range(1, 4):
        if (x-i) >= 0 and (y+i) < len(grid):
            cur = cur * grid[x-i][y+i]
    if cur > largest:
        largest = cur

    cur = grid[x][y]
    # top-right
    for i in range(1, 4):
        if (x+i) < len(grid) and (y+i) < len(grid):
            cur = cur * grid[x+i][y+i]
    if cur > largest:
        largest = cur

    cur = grid[x][y]
    # bottom-left
    for i in range(1, 4):
        if (x-i) >= 0 and (y-i) >= 0:
            cur = cur * grid[x-i][y-i]
    if cur > largest:
        largest = cur

    cur = grid[x][y]
    # bottom-left
    for i in range(1, 4):
        if (x+i) < len(grid) and (y-i) >= 0:
            cur = cur * grid[x+i][y-i]
    if cur > largest:
        largest = cur
         
# main
def main():
    grid = gridCreate()
    for x in range(0, len(grid)):
        for y in range(0, len(grid[x])):
            t = Thread(target=findLargest, args=(grid, x, y))
            t.start()
    print largest


if __name__ == '__main__':
    main()
