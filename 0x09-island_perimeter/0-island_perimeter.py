#!/usr/bin/python3
"""
Module: 0-island_perimeter
Calculates the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid.

    Args:
        grid (list of list of int): The grid representing the island and water.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all four sides
                if i == 0 or grid[i - 1][j] == 0:  # Top
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:  # Bottom
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Left
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:  # Right
                    perimeter += 1

    return perimeter
