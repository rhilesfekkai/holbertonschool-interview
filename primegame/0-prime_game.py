#!/usr/bin/python3
"""Prime Game."""


def isWinner(x, nums):
    """Determine the winner of the most rounds."""

    if x <= 0 or not nums:
        return None

    rounds = nums[:x]

    if not rounds:
        return None

    max_n = max(rounds)

    sieve = [True] * (max_n + 1)

    if max_n >= 0:
        sieve[0] = False

    if max_n >= 1:
        sieve[1] = False

    p = 2
    while p * p <= max_n:
        if sieve[p]:
            for multiple in range(p * p, max_n + 1, p):
                sieve[multiple] = False
        p += 1

    prime_count = [0] * (max_n + 1)

    for number in range(1, max_n + 1):
        prime_count[number] = (
            prime_count[number - 1] + (1 if sieve[number] else 0)
        )

    maria_wins = 0
    ben_wins = 0

    for n in rounds:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"

    if ben_wins > maria_wins:
        return "Ben"

    return None
