#!/usr/bin/python3
"""N Queens puzzle."""

import sys


def solve_nqueens(n):
    """Find all solutions to the N queens puzzle."""

    solutions = []
    positions = []

    columns = set()
    diagonals_down = set()
    diagonals_up = set()

    def backtrack(row):
        """Place queens recursively using backtracking."""

        if row == n:
            solutions.append(
                [[r, c] for r, c in positions]
            )
            return

        for col in range(n):
            diag_down = row - col
            diag_up = row + col

            if (col in columns or
                    diag_down in diagonals_down or
                    diag_up in diagonals_up):
                continue

            positions.append((row, col))
            columns.add(col)
            diagonals_down.add(diag_down)
            diagonals_up.add(diag_up)

            backtrack(row + 1)

            positions.pop()
            columns.remove(col)
            diagonals_down.remove(diag_down)
            diagonals_up.remove(diag_up)

    backtrack(0)
    return solutions


def main():
    """Validate arguments and print all solutions."""

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    for solution in solve_nqueens(n):
        print(solution)


if __name__ == "__main__":
    main()
