#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Calculate the fewest operations needed to get n H characters."""

    if not isinstance(n, int) or isinstance(n, bool) or n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor

        divisor += 1

    return operations
