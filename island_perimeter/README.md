# Island Perimeter

Calculate the perimeter of an island in a rectangular grid.

- 0 represents water.
- 1 represents land.
- Each cell has a side length of 1.

The algorithm counts four sides for each land cell
and removes sides shared with adjacent land cells.

Time complexity: O(height * width).
Space complexity: O(1).
