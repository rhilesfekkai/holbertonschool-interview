#!/usr/bin/python3
"""Log parsing statistics."""

import re
import sys


def print_stats(total_size, status_counts):
    """Print accumulated statistics."""

    print("File size: {}".format(total_size))

    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """Read stdin and compute log statistics."""

    pattern = re.compile(
        r'^\S+ - \[[^\]]+\] '
        r'"GET /projects/260 HTTP/1\.1" '
        r'(\d+) (\d+)$'
    )

    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    status_counts = {code: 0 for code in status_codes}

    total_size = 0
    line_count = 0
    last_reported = 0

    try:
        for line in sys.stdin:
            line_count += 1
            match = pattern.match(line.strip())

            if match:
                status = int(match.group(1))
                file_size = int(match.group(2))

                total_size += file_size

                if status in status_counts:
                    status_counts[status] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
                last_reported = line_count

    except KeyboardInterrupt:
        if line_count != last_reported:
            print_stats(total_size, status_counts)
        return

    if line_count > last_reported:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
