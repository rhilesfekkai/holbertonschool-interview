#!/usr/bin/python3
"""Calculate the perimeter of an island."""


def island_perimeter(grid):
    """Return the perimeter of the island described in grid."""

    perimeter = 0
    height = len(grid)

    for row in range(height):
        width = len(grid[row])

        for col in range(width):
            if grid[row][col] == 1:
                perimeter += 4

                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 1

                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 1

                if row < height - 1 and grid[row + 1][col] == 1:
                    perimeter -= 1

                if col < width - 1 and grid[row][col + 1] == 1:
                    perimeter -= 1

    return perimeter
