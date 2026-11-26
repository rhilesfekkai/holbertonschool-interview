# Log Parsing

A script that reads logs from standard input
and computes statistics.

## Statistics

- Total file size
- Number of lines by HTTP status code

## Features

- Reads stdin line by line
- Skips invalid log lines
- Prints statistics every 10 lines
- Handles keyboard interruption (CTRL + C)
- Does not execute when imported

## Usage

./0-stats.py

## Complexity

Time complexity: O(n)
Space complexity: O(1)
